from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
import subprocess
import os
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import ollama 
from typing import Dict, Any, Callable


# Load environment variables
load_dotenv()

app = FastAPI()
import subprocess
import json
from datetime import datetime
import glob
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from typing import Dict, Any, Callable

# Task functions
def install_and_run_script(package: str, script_url: str, args: list):
    """
    Install a package and run a script from a URL with provided arguments.
    """
    subprocess.run(["pip", "install", package])
    subprocess.run(["python", script_url] + args)


def format_file_with_prettier(file_path: str, prettier_version: str):
    """
    Format a file using Prettier with specific prettier version
    """
    subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])



def count_weekdays(input_file: str, output_file: str, weekday: str):
    """
    Count occurrences of a specific weekday in a file and write the count to an output file.
    """
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_index = weekdays.index(weekday)
    
    with open(input_file, "r") as file:
        dates = file.readlines()
    
    count = sum(1 for date in dates if datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == weekday_index)
    
    with open(output_file, "w") as file:
        file.write(str(count))

import json

def sort_json_by_keys(input_file: str, output_file: str, keys: list):
    """
    Sort JSON data by specified keys in specified order and write the result to an output file.
    """
    with open(input_file, "r") as file:
        data = json.load(file)
    
    sorted_data = sorted(data, key=lambda x: tuple(x[key] for key in keys))
    
    with open(output_file, "w") as file:
        json.dump(sorted_data, file)

        
def write_first_line_of_recent_logs(logs_dir: str, output_file: str, num_logs: int = 10):
    """
    Write the first line of the most recent n number of  .log files in the specified directory to an output file.
    """
    # Get all .log files in the directory
    log_files = glob.glob(os.path.join(logs_dir, "*.log"))
    
    # Sort files by modification time, most recent first
    log_files.sort(key=os.path.getmtime, reverse=True)
    
    # Take the top `num_logs` files
    recent_logs = log_files[:num_logs]
    
    # Write the first line of each file to the output file
    with open(output_file, "w") as outfile:
        for log_file in recent_logs:
            with open(log_file, "r") as infile:
                first_line = infile.readline()
                outfile.write(first_line)

import os
import glob
import json

def extract_h1_and_create_index(docs_dir: str, output_file: str):
    """
    Find all Markdown (.md) files in the specified directory, extract the first occurrence of each H1 (line starting with #),
    and create an index file mapping each filename (without the directory prefix) to its title.
    """
    # Get all .md files in the directory and its subdirectories
    md_files = glob.glob(os.path.join(docs_dir, "**", "*.md"), recursive=True)
    
    # Initialize the index dictionary
    index = {}
    
    for md_file in md_files:
        with open(md_file, "r") as file:
            # Read the file line by line
            for line in file:
                # Check if the line starts with # (H1)
                if line.startswith("# "):
                    # Extract the title (remove the # and leading/trailing whitespace)
                    title = line.lstrip("# ").strip()
                    # Get the relative path of the file (without the docs_dir prefix)
                    relative_path = os.path.relpath(md_file, docs_dir)
                    # Add the file and its title to the index
                    index[relative_path] = title
                    # Move to the next file after finding the first H1
                    break
    
    # Write the index to the output file
    with open(output_file, "w") as file:
        json.dump(index, file, indent=2)

def extract_email_address(email_content: str, output_file: str):
  """
  Extract the sender's email address from the email content and write it to the output file.
  """
  # Use an LLM to extract the email address
  """
  MAKE OPENAI  API CALL TO EXTRACT INFO Or multimodal
  """ 
  # Write the extracted email address to the output file
  with open(output_file, "w") as file:
    file.write(response)



def find_most_similar_comments(comments_file: str, output_file: str):
    # """
    # Find the most similar pair of comments using embeddings and write them to the output file.
    # """
    # # Load comments from the file
    # with open(comments_file, "r") as file:
    #     comments = file.readlines()
    
    # # Remove newline characters
    # comments = [comment.strip() for comment in comments]
    
    # # Load a pre-trained sentence transformer model
    # model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # # Generate embeddings for all comments
    # embeddings = model.encode(comments)
    
    # # Compute pairwise cosine similarity
    # similarity_matrix = cosine_similarity(embeddings)
    
    # # Find the most similar pair (excluding self-similarity)
    # np.fill_diagonal(similarity_matrix, -1)  # Ignore self-similarity
    # most_similar_indices = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)
    
    # # Get the most similar pair of comments
    # comment1 = comments[most_similar_indices[0]]
    # comment2 = comments[most_similar_indices[1]]
    
    # # Write the pair to the output file
    # with open(output_file, "w") as file:
    #     file.write(f"{comment1}\n{comment2}")
  pass

def calculate_ticket_sales(db_file: str, ticket_type: str, output_file: str):
    """
    Calculate the total sales for a specific ticket type in the SQLite database and write the result to the output file.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Query to calculate total sales for the specified ticket type
    query = """
    SELECT SUM(units * price) AS total_sales
    FROM tickets
    WHERE type = ?;
    """
    
    # Execute the query
    cursor.execute(query, (ticket_type,))
    result = cursor.fetchone()
    
    # Get the total sales value
    total_sales = result[0] if result[0] is not None else 0
    
    # Write the result to the output file
    with open(output_file, "w") as file:
        file.write(str(total_sales))
    
    # Close the database connection
    conn.close()


def extract_credit_card_number(image_path: str, output_file: str):
    """
    Extract the credit card number from the image and write it to the output file without spaces.
    """
    # Use an LLM to extract the credit card number
    response = llm.extract_credit_card_number(image_path)
    
    # Remove spaces and write the result to the output file
    with open(output_file, "w") as file:
        file.write(response.replace(" ", ""))

# Function mappings
function_mappings: Dict[str, Callable] = {
    "install_and_run_scriptn": install_and_run_script,
    "format_file_with_prettier": format_file_with_prettier,
    "count_weekdays": count_weekdays,
    "sort_json_by_keys": sort_json_by_keys,
    "write_first_line_of_recent_logs": write_first_line_of_recent_logs,
    "extract_h1_and_create_index": extract_h1_and_create_index,
    "extract_email_address": extract_email_address,
    "find_most_similar_comments": find_most_similar_comments,
    "calculate_ticket_sales": calculate_ticket_sales,
    "extract_credit_card_number": extract_credit_card_number
}
# Function schemas for OpenAI
# function_schemas = [{
#   "name": "install_and_run_script",
#   "description": "Install a package and run a script from a URL with provided arguments.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "package": {
#         "type": "string",
#         "description": "The name of the package to install."
#       },
#       "script_url": {
#         "type": "string",
#         "description": "The URL of the script to run."
#       },
#       "args": {
#         "type": "array",
#         "items": {
#           "type": "string"
#         },
#         "description": "List of arguments to pass to the script."
#       }
#     },
#     "required": ["package", "script_url", "args"]
#   }
# }
#    ,
#     {
#   "name": "format_file_with_prettier",
#   "description": "Format a file using Prettier with specific prettier version.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "file_path": {
#         "type": "string",
#         "description": "The path to the file to format."
#       },
#       "prettier_version": {
#         "type": "string",
#         "description": "The version of Prettier to use."
#       }
#     },
#     "required": ["file_path", "prettier_version"]
#   }
# },
#     {
#   "name": "count_weekdays",
#   "description": "Count occurrences of a specific weekday in a file and write the count to an output file.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "input_file": {
#         "type": "string",
#         "description": "The path to the input file containing dates."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output file to write the count."
#       },
#       "weekday": {
#         "type": "string",
#         "description": "The weekday to count (e.g., 'Wednesday')."
#       }
#     },
#     "required": ["input_file", "output_file", "weekday"]
#   }
# },
#     {
#   "name": "sort_json_by_keys",
#   "description": "Sort JSON data by specified keys in specified order and write the result to an output file.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "input_file": {
#         "type": "string",
#         "description": "The path to the input JSON file."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output JSON file."
#       },
#       "keys": {
#         "type": "array",
#         "items": {
#           "type": "string"
#         },
#         "description": "List of keys to sort by."
#       }
#     },
#     "required": ["input_file", "output_file", "keys"]
#   }
# },{
#   "name": "write_first_line_of_recent_logs",
#   "description": "Write the first line of the most recent .log files in the specified directory to an output file.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "logs_dir": {
#         "type": "string",
#         "description": "The directory containing the .log files."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output file where the first lines will be written."
#       },
#       "num_logs": {
#         "type": "integer",
#         "description": "The number of most recent log files to process."
#       }
#     },
#     "required": ["logs_dir", "output_file","num_logs"]
#   }
# },
# {
#   "name": "extract_h1_and_create_index",
#   "description": "Find all Markdown (.md) files in the specified directory, extract the first occurrence of each H1 (line starting with #), and create an index file mapping each filename (without the directory prefix) to its title.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "docs_dir": {
#         "type": "string",
#         "description": "The directory containing the Markdown files."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output JSON file where the index will be written."
#       }
#     },
#     "required": ["docs_dir", "output_file"]
#   }
# },
# {
#   "name": "extract_email_address",
#   "description": "Extract the sender's email address from the email content and write it to the output file.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "email_content": {
#         "type": "string",
#         "description": "The content of the email."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output file where the email address will be written."
#       }
#     },
#     "required": ["email_content", "output_file"]
#   }
# },
# {
#   "name": "extract_credit_card_number",
#   "description": "Extract the credit card number from the image and write it to the output file without spaces.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "image_path": {
#         "type": "string",
#         "description": "The path to the image containing the credit card number."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output file where the credit card number will be written."
#       }
#     },
#     "required": ["image_path", "output_file"]
#   }
# },
# {
#   "name": "find_most_similar_comments",
#   "description": "Find the most similar pair of comments using embeddings and write them to the output file.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "comments_file": {
#         "type": "string",
#         "description": "The path to the file containing the list of comments."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output file where the most similar pair of comments will be written."
#       }
#     },
#     "required": ["comments_file", "output_file"]
#   }
# },
# {
#   "name": "calculate_ticket_sales",
#   "description": "Calculate the total sales for a specific ticket type in the SQLite database and write the result to the output file.",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "db_file": {
#         "type": "string",
#         "description": "The path to the SQLite database file."
#       },
#       "ticket_type": {
#         "type": "string",
#         "description": "The ticket type for which total sales will be calculated."
#       },
#       "output_file": {
#         "type": "string",
#         "description": "The path to the output file where the total sales will be written."
#       }
#     },
#     "required": ["db_file", "ticket_type", "output_file"]
#   }
# }

# ]


# Initialize OpenAI client
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define function mappings and schemas (from previous implementation)

# def parse_task_description(task_description: str):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant that parses task descriptions into structured tasks."},
#             {"role": "user", "content": task_description}
#         ],
#         functions=function_schemas,
#         function_call="required"
#     )
#     return response.choices[0].message

# def parse_task_description(task_description: str):
#     response = ollama.chat(
#     'qwen2.5:3b',
#     messages=[{'role': 'user', 'content': task_description}],
#     tools=[install_and_run_script])
#     print("000"*10)
#     print(response)
#     print("000"*10)

def execute_function_call(function_call):
    function_name = function_call.name
    function_args = json.loads(function_call.arguments)
    function_to_call = function_mappings.get(function_name)
    if function_to_call:
        function_to_call(**function_args)
    else:
        raise ValueError(f"Function {function_name} not found")

@app.post("/run")
async def run_task(task: str = Query(..., description="Plain-English task description")):
    # try:
    #     function_call = parse_task_description(task).function_call
    #     execute_function_call(function_call)
    #     return {"status": "success", "message": "Task executed successfully"}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
        response = ollama.chat(
            'qwen2.5:3b',
            messages=[{'role': 'user', 'content': task}],
            tools=[install_and_run_script])
        print("000"*10)
        print(response)
        print("000"*10)

@app.get("/read")
async def read_file(path: str = Query(..., description="Path to the file to read")):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r") as file:
        content = file.read()
    return {"content": content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)