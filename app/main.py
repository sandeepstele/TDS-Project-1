# /// script
# dependencies = [
#   "fastapi",
#   "requests",
# ]
# ///




from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import PlainTextResponse
import os
import logging
from typing import Dict, Callable
from funtion_tasks import (
format_file_with_prettier,
query_gpt,
query_gpt_image, 
query_database, 
extract_specific_text_using_llm, 
get_embeddings, 
get_similar_text_using_embeddings, 
extract_text_from_image, 
extract_specific_content_and_create_index, 
process_and_write_logfiles, 
sort_json_by_keys, 
count_occurrences, 
install_and_run_script
)


load_dotenv()
app = FastAPI()

RUNNING_IN_CODESPACES = "CODESPACES" in os.environ
RUNNING_IN_DOCKER = os.path.exists("/.dockerenv")


def ensure_local_path(path: str) -> str:
    """Ensure the path uses './data/...' locally, but '/data/...' in Docker."""
    if ((not RUNNING_IN_CODESPACES) and RUNNING_IN_DOCKER): 
        print("IN HERE",RUNNING_IN_DOCKER) # If absolute Docker path, return as-is :  # If absolute Docker path, return as-is
        return path
    
    else:
        logging.info(f"Inside ensure_local_path with path: {path}")
        return path.lstrip("/")  # If absolute local path, remove leading slash
        # return "."+path
        #return os.path.join("./", path)  

function_mappings: Dict[str, Callable] = {
"install_and_run_script": install_and_run_script, 
"format_file_with_prettier": format_file_with_prettier,
"query_database":query_database, 
"extract_specific_text_using_llm":extract_specific_text_using_llm, 
'get_embeddings':get_embeddings, 
'get_similar_text_using_embeddings':get_similar_text_using_embeddings, 
'extract_text_from_image':extract_text_from_image, 
"extract_specific_content_and_create_index":extract_specific_content_and_create_index, 
"process_and_write_logfiles":process_and_write_logfiles, 
"sort_json_by_keys":sort_json_by_keys, 
'count_occurrences':count_occurrences
}

def parse_task_description(task_description: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that parses task descriptions into structured tasks."},
            {"role": "user", "content": task_description}
        ],
        functions=function_schemas,
        function_call="required"
    )
    return response.choices[0].message


def execute_function_call(function_call):
    logging.info(f"Inside execute_function_call with function_call: {function_call}")
    try:
        function_name = function_call.name
        function_args = function_call.arguments
        function_to_call = function_mappings.get(function_name)
        print('Calling function:', function.name)
        print('Arguments:', function_args)
        print('Function output:', function_to_call(**tool.function.arguments))
        if function_to_call:
            function_to_call(**function_args)
        else:
            raise ValueError(f"Function {function_name} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e), message="Error executing function in execute_function_call(")

@app.post("/run")
async def run_task(task: str = Query(..., description="Plain-English task description")):
    logging.info(f"Inside run_task with task: {task}")
    try:
        function_call_response = parse_task_description(task)
        if function_call_response.message.tool_calls:
            for tool in function_call_response.message.tool_calls:
                execute_function_call(tool.function)
        return {"status": "success", "message": "Task executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e), message="Error executing task in run_task")


@app.get("/read",response_class=PlainTextResponse)
async def read_file(path: str = Query(..., description="Path to the file to read")):
    logging.info(f"Inside read_file with path: {path}")
    output_file_path = ensure_local_path(path)
    if not os.path.exists(output_file_path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(output_file_path, "r") as file:
        content = file.read()
        print(content)
    return content

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)