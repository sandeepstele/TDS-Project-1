import dotenv
import glob
import requests
import os
import json
from dateutil.parser import parse
import re
from pathlib import Path
dotenv.load_dotenv()
API_KEY = os.getenv("OPEN_AI_PROXY_TOKEN")
URL_CHAT = os.getenv("OPEN_AI_PROXY_URL")
URL_EMBEDDING = os.getenv("OPEN_AI_EMBEDDING_URL")
import inspect
from typing import Callable, get_type_hints, Dict, Any, Tuple,Optional,List
from pydantic import create_model, BaseModel
import docstring_parser
import httpx
import ollama
import inspect
import subprocess
RUNNING_IN_CODESPACES = "CODESPACES" in os.environ
RUNNING_IN_DOCKER = os.path.exists("/.dockerenv")


def ensure_local_path(path: str) -> str:
    """Ensure the path uses './data/...' locally, but '/data/...' in Docker."""
    if ((not RUNNING_IN_CODESPACES) and RUNNING_IN_DOCKER): 
        print("IN HERE",RUNNING_IN_DOCKER) # If absolute Docker path, return as-is :  # If absolute Docker path, return as-is
        return path
    
    else:
        print("OUT HERE")
        return path.lstrip("/")  # If absolute local path, remove leading slash
        # return "."+path
        #return os.path.join("./", path)  


def convert_function_to_openai_schema(func: Callable) -> dict:
    """
    Converts a Python function into an OpenAI function schema with strict JSON schema enforcement.

    Args:
        func (Callable): The function to convert.

    Returns:
        dict: The OpenAI function schema.
    """
    # Extract the function's signature
    sig = inspect.signature(func)
    
    # Extract type hints
    type_hints = get_type_hints(func)
    
    # Create a Pydantic model dynamically based on the function's parameters
    fields = {
        name: (type_hints.get(name, Any), ...)
        for name in sig.parameters
    }
    PydanticModel = create_model(func.__name__ + "Model", **fields)
    
    # Generate the JSON schema from the Pydantic model
    schema = PydanticModel.model_json_schema()
    
    # Parse the function's docstring
    docstring = inspect.getdoc(func) or ""
    parsed_docstring = docstring_parser.parse(docstring)
    
    # Extract parameter descriptions
    param_descriptions = {
        param.arg_name: param.description or ""
        for param in parsed_docstring.params
    }
    
    # Update the schema with descriptions and set additionalProperties to False
    for prop_name, prop in schema.get('properties', {}).items():
        prop['description'] = param_descriptions.get(prop_name, '')
        
        # Ensure 'items' has a 'type' key for array properties
        if prop.get('type') == 'array' and 'items' in prop:
            if not isinstance(prop['items'], dict) or 'type' not in prop['items']:
                # Default to array of strings if type is not specified
                prop['items'] = {'type': 'string'}
    
    schema['additionalProperties'] = False
    
    # Ensure 'required' field is present and includes all parameters
    schema['required'] = list(fields.keys())
    
    # Construct the final OpenAI function schema
    openai_function_schema = {
        'type': 'function',
        'function':{
        'name': func.__name__,
        'description': parsed_docstring.short_description or '',
        'parameters': {
            'type': 'object',
            'properties': schema.get('properties', {}),
            'required': schema.get('required', []),
            'additionalProperties': schema.get('additionalProperties', False),
        },
        'strict': True,
    }
    }
    
    return openai_function_schema

# print(Path("/data/info.md"))
# del_path = Path("data/something.md")
# print(del_path)
# with open(del_path, "r") as file:
#     print(file.read())
# # Example usage
# def query_database(db_file: str, output_file: str, query: str, query_params: tuple):
#     """
#     query_database

#     Args:
#         db_file (str): The path to the SQLite database file.
#         output_file (str): The path to the output file where the result will be written.
#         query (str): The SQL query to execute.
#         query_params (tuple): The parameters to pass to the query.

#     Returns:
#         None
#     """
#     db_file_path = ensure_local_path(db_file)
#     output_file_path = ensure_local_path(output_file)
#     # Connect to the SQLite database
#     conn = sqlite3.connect(db_file_path)
#     cursor = conn.cursor()

    
#     # # Query to calculate total sales for the specified ticket type
#     # query = """
#     # SELECT SUM(units * price) AS total_sales
#     # FROM tickets
#     # WHERE type = ?;
#     # """
    
#     # Execute the query
#     cursor.execute(query, (query_params))
#     result = cursor.fetchone()
    
#     # Get the total sales value
#     total_sales = result[0] if result[0] is not None else 0
    
#     # Write the result to the output file
#     with open(output_file_path, "w") as file:
#         file.write(str(total_sales))
    
#     # Close the database connection
#     conn.close()
import sqlite3
from typing import Tuple 
def query_gpt(user_input: str, system_message: str):
    print("🔍 User Input:", user_input)
    response = requests.post(
        URL_CHAT,
        headers={"Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"},
        json={
            "model": "gpt-4o-mini",
            "messages":[{'role': 'system','content': system_message},
                        {'role': 'user', 'content': user_input}]
        }
    )
    response.raise_for_status()
    result = response.json()
import base64
def query_gpt_image(image_path: str, system_message: str):
    print("🔍 Image Path:", image_path)
    image_format = image_path.split(".")[-1]
    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")
    response = requests.post(
        URL_CHAT,
        headers={"Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract text from this image"},
                    {
                    "type": "image_url",
                    "image_url": { "url": f"data:image/{image_format};base64,{image_data}" }
                    }
                ]
                }
            ]
            }
                     )
    response.raise_for_status()
    result = response.json()    
def query_database(db_file: str, output_file: str, query: str, query_params: Tuple):
    """
    Executes a SQL query on the specified SQLite database and writes the result to an output file.

    Args:
        db_file (str): The path to the SQLite database file.
        output_file (str): The path to the output file where the result will be written.
        query (str): The SQL query to execute.
        query_params (Tuple): The parameters to pass to the query in order to the query

    Returns:
        None
    """
    # Ensure the database and output file paths are correct
    db_file_path = ensure_local_path(db_file)
    output_file_path = ensure_local_path(output_file)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    try:
        # Execute the query with the provided parameters
        cursor.execute(query, query_params)
        result = cursor.fetchone()

        # Assuming the query returns a single value (e.g., total_sales)
        if result:
            output_data = result[0]
        else:
            output_data = 'No results found.'

        # Write the result to the output file
        with open(output_file_path, "w") as file:
            file.write(str(output_data))

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        conn.close()
def extract_specific_text(input_file: str, output_file: str, task: str):
    """
    Extracts specific text from a file using an LLM and writes it to an output file.

    Args:
        input_file (str): The file that contains the text to extract.
        output_file (str): The path to the output file where the extracted text will be written.
        task(str): The task that specifies the text to extract.
    Returns:
        None
    """
    # Write the extracted email address to the output file
    input_file_path = ensure_local_path(input_file)
    with open(input_file_path, "r") as file:
        text_info = file.read() #readlines gives list, this gives string
    print(text_info)
    output_file_path = ensure_local_path(output_file)
    response = query_gpt(text_info, task)
    print("000"*10)
    print(response)
    print("000"*10)
    with open(output_file_path, "w") as file:
        file.write(response.message.content)
def get_embeddings(texts: List[str]):
    # headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    # payload = {"model": "text-embedding-3-small", "input": texts}
    # response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    # response.raise_for_status()
    response = ollama.embed(
        model='nomic-embed-text:latest',
        input=texts
        )
    # return [item["embedding"] for item in response.json()["data"]]
    return response["embeddings"]
def get_similar_text_using_embeddings(input_file: str, output_file: str, no_of_similar_texts: int):
    """
    From a given input file, reads each line as a list and finds the most number of similar texts no_of_similar_texts(Eg File containing comments) using embeddings and cosine similarty and writes them to the output file in the order of similarity if specified.

    Args:
        input_file (str): The file that contains lines to find similar.
        output_file (str): The path to the output file where the ouput text will be written.
        no_of_similar_texts (int): The number of similar texts to find.
    Returns:
        None
    """
    input_file_path = ensure_local_path(input_file)

    # Load comments from the file
    with open(input_file_path, "r") as file:
        documents = file.readlines()
    
    # Remove newline characters
    documents = [comment.strip() for comment in documents]
    
    # Load a pre-trained sentence transformer model
    line_embeddings = get_embeddings(documents)
    
    
    # Compute pairwise cosine similarity
    similarity_matrix = cosine_similarity(line_embeddings)
    
    # Find the most similar pair (excluding self-similarity)
    np.fill_diagonal(similarity_matrix, -1)  # Ignore self-similarity
    most_similar_indices = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)
    
    # Get the most n similar texts
    similar_texts = []
    for i in range(no_of_similar_texts):
        similar_texts.append(documents[most_similar_indices[i]])

    # Write the them to the output file
    with open(output_file, "w") as file:
        for text in similar_texts:
            file.write(text + "\n")
def extract_text_from_image(image_path: str, output_file: str):
    """
    Extract the text from the image and write it to the output file without spaces.

    Args:
        image_path (str): The path to the image file.
        output_file (str): The path to the output file where the extracted text will be written.
    Returns:
        None
    """
    # Use an LLM to extract the credit card number
    # response = llm.extract_credit_card_number(image_path)
    image_path___ = ensure_local_path(image_path)
    response = query_gpt(image_path___, "Extract the text from the image")
    
    output_file_path = ensure_local_path(output_file) 
    # Remove spaces and write the result to the output file
    print(response.choices[0].message.content)
    with open(output_file_path, "w") as file:
        file.write(response.choices[0].message.content.replace(" ", ""))       
def extract_specific_content_and_create_index(input_file: str, output_file: str, extension: str,content_marker: str):
    """
    Identify all files with a specific extension in a directory.For each file, extract particular content (e.g., the first occurrence of a header) and create an index file mapping filenames to their extracted content.
    
    Args:
        input_file (str): The directory containing the files to index.
        output_file (str): The path to the output file where the index will be written.
        extension (str): The file extension to filter files.
        content_marker (str): The content marker to extract from each file.
    """
    input_file_path = ensure_local_path(input_file)
    output_file_path = ensure_local_path(output_file)

    extenstion_files = glob.glob(os.path.join(input_file_path, "**", f"*.{extension}"), recursive=True)
    
    index = {}

    for extenstion_file in extenstion_files:
        title = None
        with open(extenstion_file, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(content_marker):
                    title = line.lstrip(content_marker).strip()
                    break  # Stop reading after first H1

        # Compute relative path
        relative_path = os.path.relpath(extenstion_file, input_file_path)

        # Store in index (even if no H1 is found)
        index[relative_path] = title if title else ""

    # Write to JSON file
    with open(output_file_path, "w", encoding="utf-8") as json_file:
        json.dump(index, json_file, indent=2, sort_keys=True)
def process_and_write_logfiles(input_file: str, output_file: str, num_logs: int = 10, num_of_lines: int = 1):
    """
    Process n number of log files num_logs given in the input_file and write x number of lines num_of_lines  of each log file to the output_file.
    
    Args:
        input_file (str): The directory containing the log files.
        output_file (str): The path to the output file where the extracted lines will be written.
        num_logs (int): The number of log files to process.
        num_of_lines (int): The number of lines to extract from each log file.

    """
    # Get all .log files in the directory
    input_file_path = ensure_local_path(input_file)
    output_file_path = ensure_local_path(output_file) 
    log_files = glob.glob(os.path.join(logs_dir_path, "*.log"))
    
    # Sort files by modification time, most recent first
    log_files.sort(key=os.path.getmtime, reverse=True)
    
    # Take the top `num_logs` files
    recent_logs = log_files[:num_logs]
    
    # Write the first line of each file to the output file
    with open(output_file_path, "w") as outfile:
        for log_file in recent_logs:
            with open(log_file, "r") as infile:
                for _ in range(num_of_lines):
                    line = infile.readline()
                    if line:
                        outfile.write(line)
                    else:
                        break
def sort_json_by_keys(input_file: str, output_file: str, keys: list):
    """
    Sort JSON data by specified keys in specified order and write the result to an output file.
    Args:
        input_file (str): The path to the input JSON file.
        output_file (str): The path to the output JSON file.
        keys (list): The keys to sort the JSON data by.
    """
    input_file_path = ensure_local_path(input_file)
    output_file_path = ensure_local_path(output_file) 
    with open(input_file_path, "r") as file:
        data = json.load(file)
    
    sorted_data = sorted(data, key=lambda x: tuple(x[key] for key in keys))
    
    with open(output_file_path, "w") as file:
        json.dump(sorted_data, file)                       
def count_occurrences(
    input_file: str,
    output_file: str,
    date_component: Optional[str] = None,
    target_value: Optional[int] = None,
    custom_pattern: Optional[str] = None
):
    """
    Count occurrences of specific date components or custom patterns in a file and write the count to an output file.
    Handles various date formats automatically.

    Parameters:
        input_file (str): Path to the input file containing dates or text lines.
        output_file (str): Path to the output file where the count will be written.
        date_component (Optional[str]): The date component to check ('weekday', 'month', 'year', 'leap_year').
        target_value (Optional[int]): The target value for the date component (e.g., 0 for Monday, 1 for January, 2025 for year).
        custom_pattern (Optional[str]): A regex pattern to search for in each line.
    """  
    count = 0
    input_file_path = ensure_local_path(input_file)
    output_file_path = ensure_local_path(output_file)
    with open(input_file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            # Check for custom pattern
            if custom_pattern and re.search(custom_pattern, line):
                count += 1
                continue

            # Attempt to parse the date
            try:
                parsed_date = parse(line)  # Auto-detect format
            except (ValueError, OverflowError):
                print(f"Skipping invalid date format: {line}")
                continue

            # Check for specific date components
            if date_component == 'weekday' and parsed_date.weekday() == target_value:
                count += 1
            elif date_component == 'month' and parsed_date.month == target_value:
                count += 1
            elif date_component == 'year' and parsed_date.year == target_value:
                count += 1
            elif date_component == 'leap_year' and parsed_date.year % 4 == 0 and (parsed_date.year % 100 != 0 or parsed_date.year % 400 == 0):
                count += 1

    # Write the result to the output file
    with open(output_file_path, "w") as file:
        file.write(str(count))
def install_and_run_script(package: str, script_url: str, args: list):
    """
    Install a package and download a script from a URL with provided arguments and run it with python
    Args:
        package (str): The package to install.
        script_url (str): The URL to download the script from.
        args (list): The arguments to pass to the script and run it
    """
    subprocess.run(["pip", "install", package])
    subprocess.run(["curl", "-O", script_url]+ args)
    script_name = script_url.split("/")[-1]
    print("111"*10)
    print(script_name)
    print("111"*10)
    subprocess.run(["uv","run", script_name,args[0]])

# Convert the function to an OpenAI schema
schema = convert_function_to_openai_schema(count_occurrences)
# print(schema)


# Define the data payload
# def query_gpt_with_tools(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
#     print("🔍 User Input:", user_input)
#     response = requests.post(
#         "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
#         headers={"Authorization": f"Bearer {API_KEY}",
#                 "Content-Type": "application/json"},
#         json={
#             "model": "gpt-4o-mini",
#             "messages": [
#                 {"role": "user", "content": user_input}
#             ],
#             "tools": tools,
#             "tool_choice": "required"
#         }
#     )
#     result = response.json()
#     # response = httpx.post(
#     #     "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
#     #     headers={
#     #         "Authorization": f"Bearer {API_KEY}",
#     #         "Content-Type": "application/json",
#     #     },
#     #     json={
#     #         "model": "gpt-4o-mini",
#     #         "messages": [{"role": "user", "content": user_input}],
#     #         "tools": tools,
#     #         "tool_choice": "required",
#     #     },
#     # )
#     print("🔍 Full Response:", result)
#     return response.json()["choices"][0]["message"]["tool_calls"][0]["function"]


# if __name__ == "__main__":
#     prompt = """The SQLite database file /data/ticket-sales.db has a tickets with columns type, units, and price. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the “Gold” ticket type? Write the number in /data/ticket-sales-gold.txt"""
#     response = query_gpt(prompt, [schema])
#     print(response)
#     #print([tool_call["function"] for tool_call in response["tool_calls"]])