import subprocess
from pathlib import Path
import os
import os
import json

# RUNNING_IN_CODESPACES = "CODESPACES" in os.environ
# RUNNING_IN_DOCKER = os.path.exists("/.dockerenv")


# def ensure_local_path(path: str) -> str:
#     """Ensure the path uses './data/...' locally, but '/data/...' in Docker."""
#     if ((not RUNNING_IN_CODESPACES) and RUNNING_IN_DOCKER): 
#         print("IN HERE",RUNNING_IN_DOCKER) # If absolute Docker path, return as-is :  # If absolute Docker path, return as-is
#         return path
    
#     else:
#         print("OUT HERE")
#         return path.lstrip("/")  # If absolute local path, remove leading slash
#         # return "."+path
#         #return os.path.join("./", path) 
# def check_valid_file_path(file_path: str) -> bool:
#     """
#     Check if the file path is valid
#     """
#     return Path(file_path).exists()
# def format_file_with_prettier(file_path: str, prettier_version: str):
#     """
#     Format a file using Prettier with specific prettier version
#     """
    
#     subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])

# file_path = "/data/format.md"
# input_path = ensure_local_path(file_path)
# print(input_path)
# if check_valid_file_path(input_path):

#     format_file_with_prettier(input_path, "3.4.2")
# else:
#     print("Invalid file path")




# a = [{'first_name': 'Cameron', 'last_name': 'Adams', 'email': 'walteralvarado@example.org'}, {'first_name': 'William', 'last_name': 'Adams', 'email': 'kathrynrobertson@example.org'}, {'first_name': 'Melissa', 'last_name': 'Aguilar', 'email': 'andrew01@example.net'}, {'first_name': 'Roy', 'last_name': 'Anderson', 'email': 'hurstcalvin@example.org'}, {'first_name': 'Wendy', 'last_name': 'Andrews', 'email': 'teresastewart@example.net'}, {'first_name': 'Stephanie', 'last_name': 'Atkins', 'email': 'chase71@example.com'}, {'first_name': 'Joseph', 'last_name': 'Barton', 'email': 'williamsjessica@example.org'}, {'first_name': 'Natalie', 'last_name': 'Bass', 'email': 'vclark@example.com'}, {'first_name': 'Carlos', 'last_name': 'Bennett', 'email': 'dustinbarrett@example.net'}, {'first_name': 'Anthony', 'last_name': 'Bishop', 'email': 'leslie85@example.com'}, {'first_name': 'Jonathan', 'last_name': 'Bradley', 'email': 'marshallbrian@example.com'}, {'first_name': 'Randy', 'last_name': 'Bridges', 'email': 'smithtimothy@example.com'}, {'first_name': 'Henry', 'last_name': 'Brown', 'email': 'dustin07@example.com'}, {'first_name': 'Jeffrey', 'last_name': 'Bush', 'email': 'victoria20@example.com'}, {'first_name': 'Kevin', 'last_name': 'Cain', 'email': 'joshuapittman@example.com'}, {'first_name': 'Sean', 'last_name': 'Cameron', 'email': 'daveoconnor@example.org'}, {'first_name': 'Christopher', 'last_name': 'Cobb', 'email': 'kdouglas@example.com'}, {'first_name': 'Sophia', 'last_name': 'Collins', 'email': 'longsarah@example.org'}, {'first_name': 'Jeffery', 'last_name': 'Cook', 'email': 'martinalex@example.net'}, {'first_name': 'James', 'last_name': 'Curtis', 'email': 'gortega@example.com'}, {'first_name': 'Madison', 'last_name': 'Daniels', 'email': 'matthew63@example.net'}, {'first_name': 'Michael', 'last_name': 'Edwards', 'email': 'shawn01@example.com'}, {'first_name': 'Jeffrey', 'last_name': 'Estrada', 'email': 'toni47@example.net'}, {'first_name': 'Thomas', 'last_name': 'Fitzgerald', 'email': 'johnsondillon@example.org'}, {'first_name': 'Troy', 'last_name': 'Flores', 'email': 'othompson@example.org'}, {'first_name': 'Roberta', 'last_name': 'Foster', 'email': 'thomasjones@example.com'}, {'first_name': 'Patricia', 'last_name': 'Freeman', 'email': 'laurasolomon@example.net'}, {'first_name': 'Ricky', 'last_name': 'Frost', 'email': 'ypierce@example.org'}, {'first_name': 'Elaine', 'last_name': 'Fuller', 'email': 'jade79@example.com'}, {'first_name': 'Christian', 'last_name': 'Garcia', 'email': 'henry41@example.net'}, {'first_name': 'James', 'last_name': 'Garcia', 'email': 'sgonzalez@example.com'}, {'first_name': 'Lorraine', 'last_name': 'Garcia', 'email': 'logan46@example.com'}, {'first_name': 'Ivan', 'last_name': 'Gilbert', 'email': 'davischris@example.net'}, {'first_name': 'Sandy', 'last_name': 'Gomez', 'email': 'qjones@example.net'}, {'first_name': 'Robert', 'last_name': 'Gonzalez', 'email': 'angela55@example.org'}, {'first_name': 'Christina', 'last_name': 'Grant', 'email': 'shanecastillo@example.net'}, {'first_name': 'Kathleen', 'last_name': 'Hall', 'email': 'sbowman@example.com'}, {'first_name': 'David', 'last_name': 'Hardy', 'email': 'wjackson@example.net'}, {'first_name': 'Lisa', 'last_name': 'Hardy', 'email': 'vbaldwin@example.org'}, {'first_name': 'Kathleen', 'last_name': 'Harrington', 'email': 'brownalexandra@example.com'}, {'first_name': 'Jessica', 'last_name': 'Henry', 'email': 'zachary11@example.org'}, {'first_name': 'Gregory', 'last_name': 'Hernandez', 'email': 'vjenkins@example.net'}, {'first_name': 'John', 'last_name': 'Hernandez', 'email': 'vcameron@example.org'}, {'first_name': 'James', 'last_name': 'Huang', 'email': 'eparker@example.net'}, {'first_name': 'Jennifer', 'last_name': 'Hubbard', 'email': 'nbrown@example.net'}, {'first_name': 'Joshua', 'last_name': 'Huerta', 'email': 'tamara54@example.net'}, {'first_name': 'David', 'last_name': 'Jackson', 'email': 'rachelwood@example.org'}, {'first_name': 'Nicole', 'last_name': 'Jennings', 'email': 'nguyengary@example.org'}, {'first_name': 'Reginald', 'last_name': 'Jones', 'email': 'aedwards@example.org'}, {'first_name': 'Jerry', 'last_name': 'Jordan', 'email': 'qmorgan@example.net'}, {'first_name': 'Marcia', 'last_name': 'Kemp', 'email': 'bentleymelissa@example.com'}, {'first_name': 'Bryan', 'last_name': 'Krueger', 'email': 'gedwards@example.org'}, {'first_name': 'Regina', 'last_name': 'Lawson', 'email': 'pallen@example.org'}, {'first_name': 'Becky', 'last_name': 'Lee', 'email': 'catherinecampbell@example.com'}, {'first_name': 'Marissa', 'last_name': 'Lewis', 'email': 'pmiller@example.net'}, {'first_name': 'Mark', 'last_name': 'Lewis', 'email': 'kristinlynn@example.net'}, {'first_name': 'James', 'last_name': 'Li', 'email': 'aaronjackson@example.net'}, {'first_name': 'Tiffany', 'last_name': 'Lopez', 'email': 'harrisbriana@example.com'}, {'first_name': 'Angela', 'last_name': 'Lucas', 'email': 'luke05@example.com'}, {'first_name': 'Amanda', 'last_name': 'Mason', 'email': 'clarkbrandon@example.com'}, {'first_name': 'Matthew', 'last_name': 'Mayo', 'email': 'amullen@example.net'}, {'first_name': 'Tammy', 'last_name': 'Mcgrath', 'email': 'lauraolson@example.org'}, {'first_name': 'Shelley', 'last_name': 'Mitchell', 'email': 'xperez@example.com'}, {'first_name': 'Karen', 'last_name': 'Moran', 'email': 'cynthiamorrison@example.com'}, {'first_name': 'Christy', 'last_name': 'Morrison', 'email': 'angela11@example.net'}, {'first_name': 'Jeffrey', 'last_name': 'Mullen', 'email': 'lanejason@example.net'}, {'first_name': 'Larry', 'last_name': 'Norris', 'email': 'phillip89@example.com'}, {'first_name': 'Michael', 'last_name': 'Oliver', 'email': 'aprilbrown@example.net'}, {'first_name': 'Monica', 'last_name': 'Olson', 'email': 'caseynancy@example.com'}, {'first_name': 'Nancy', 'last_name': 'Ortiz', 'email': 'melendezchristopher@example.org'}, {'first_name': 'Benjamin', 'last_name': 'Owens', 'email': 'markjohnson@example.org'}, {'first_name': 'Edward', 'last_name': 'Park', 'email': 'jennifer44@example.com'}, {'first_name': 'Edward', 'last_name': 'Patton', 'email': 'monica48@example.org'}, {'first_name': 'Timothy', 'last_name': 'Pittman', 'email': 'josephmurillo@example.com'}, {'first_name': 'Gina', 'last_name': 'Powers', 'email': 'stephanie45@example.org'}, {'first_name': 'Kara', 'last_name': 'Ramirez', 'email': 'frankpugh@example.com'}, {'first_name': 'Sabrina', 'last_name': 'Ramirez', 'email': 'susanchavez@example.org'}, {'first_name': 'Bill', 'last_name': 'Reed', 'email': 'zpatel@example.com'}, {'first_name': 'Kevin', 'last_name': 'Reynolds', 'email': 'roger56@example.net'}, {'first_name': 'Paul', 'last_name': 'Rice', 'email': 'jennahill@example.com'}, {'first_name': 'Amanda', 'last_name': 'Riley', 'email': 'donna65@example.com'}, {'first_name': 'Heather', 'last_name': 'Robinson', 'email': 'zhowell@example.com'}, {'first_name': 'Heather', 'last_name': 'Romero', 'email': 'wgordon@example.org'}, {'first_name': 'Justin', 'last_name': 'Ruiz', 'email': 'patricia84@example.net'}, {'first_name': 'Dana', 'last_name': 'Savage', 'email': 'martinkimberly@example.org'}, {'first_name': 'Heather', 'last_name': 'Sims', 'email': 'david14@example.org'}, {'first_name': 'Jeffrey', 'last_name': 'Smith', 'email': 'lee75@example.net'}, {'first_name': 'Megan', 'last_name': 'Stevens', 'email': 'davismichelle@example.org'}, {'first_name': 'Lisa', 'last_name': 'Tanner', 'email': 'josephgreen@example.com'}, {'first_name': 'Deborah', 'last_name': 'Tate', 'email': 'abennett@example.net'}, {'first_name': 'Hannah', 'last_name': 'Taylor', 'email': 'klee@example.net'}, {'first_name': 'Terri', 'last_name': 'Taylor', 'email': 'prestongary@example.com'}, {'first_name': 'Crystal', 'last_name': 'Terry', 'email': 'carrerika@example.net'}, {'first_name': 'David', 'last_name': 'Thomas', 'email': 'stephanie52@example.com'}, {'first_name': 'Kenneth', 'last_name': 'Valdez', 'email': 'dunnkaitlin@example.com'}, {'first_name': 'Amy', 'last_name': 'Walker', 'email': 'adamsutton@example.com'}, {'first_name': 'Stephen', 'last_name': 'Wall', 'email': 'phillipsmelissa@example.net'}, {'first_name': 'Kevin', 'last_name': 'Waller', 'email': 'qvaughn@example.org'}, {'first_name': 'Diane', 'last_name': 'Williams', 'email': 'hmack@example.org'}, {'first_name': 'Andrea', 'last_name': 'Wu', 'email': 'tschultz@example.com'}]

# b = [{"first_name": "Cameron", "last_name": "Adams", "email": "walteralvarado@example.org"}, {"first_name": "William", "last_name": "Adams", "email": "kathrynrobertson@example.org"}, {"first_name": "Melissa", "last_name": "Aguilar", "email": "andrew01@example.net"}, {"first_name": "Roy", "last_name": "Anderson", "email": "hurstcalvin@example.org"}, {"first_name": "Wendy", "last_name": "Andrews", "email": "teresastewart@example.net"}, {"first_name": "Stephanie", "last_name": "Atkins", "email": "chase71@example.com"}, {"first_name": "Joseph", "last_name": "Barton", "email": "williamsjessica@example.org"}, {"first_name": "Natalie", "last_name": "Bass", "email": "vclark@example.com"}, {"first_name": "Carlos", "last_name": "Bennett", "email": "dustinbarrett@example.net"}, {"first_name": "Anthony", "last_name": "Bishop", "email": "leslie85@example.com"}, {"first_name": "Jonathan", "last_name": "Bradley", "email": "marshallbrian@example.com"}, {"first_name": "Randy", "last_name": "Bridges", "email": "smithtimothy@example.com"}, {"first_name": "Henry", "last_name": "Brown", "email": "dustin07@example.com"}, {"first_name": "Jeffrey", "last_name": "Bush", "email": "victoria20@example.com"}, {"first_name": "Kevin", "last_name": "Cain", "email": "joshuapittman@example.com"}, {"first_name": "Sean", "last_name": "Cameron", "email": "daveoconnor@example.org"}, {"first_name": "Christopher", "last_name": "Cobb", "email": "kdouglas@example.com"}, {"first_name": "Sophia", "last_name": "Collins", "email": "longsarah@example.org"}, {"first_name": "Jeffery", "last_name": "Cook", "email": "martinalex@example.net"}, {"first_name": "James", "last_name": "Curtis", "email": "gortega@example.com"}, {"first_name": "Madison", "last_name": "Daniels", "email": "matthew63@example.net"}, {"first_name": "Michael", "last_name": "Edwards", "email": "shawn01@example.com"}, {"first_name": "Jeffrey", "last_name": "Estrada", "email": "toni47@example.net"}, {"first_name": "Thomas", "last_name": "Fitzgerald", "email": "johnsondillon@example.org"}, {"first_name": "Troy", "last_name": "Flores", "email": "othompson@example.org"}, {"first_name": "Roberta", "last_name": "Foster", "email": "thomasjones@example.com"}, {"first_name": "Patricia", "last_name": "Freeman", "email": "laurasolomon@example.net"}, {"first_name": "Ricky", "last_name": "Frost", "email": "ypierce@example.org"}, {"first_name": "Elaine", "last_name": "Fuller", "email": "jade79@example.com"}, {"first_name": "Christian", "last_name": "Garcia", "email": "henry41@example.net"}, {"first_name": "James", "last_name": "Garcia", "email": "sgonzalez@example.com"}, {"first_name": "Lorraine", "last_name": "Garcia", "email": "logan46@example.com"}, {"first_name": "Ivan", "last_name": "Gilbert", "email": "davischris@example.net"}, {"first_name": "Sandy", "last_name": "Gomez", "email": "qjones@example.net"}, {"first_name": "Robert", "last_name": "Gonzalez", "email": "angela55@example.org"}, {"first_name": "Christina", "last_name": "Grant", "email": "shanecastillo@example.net"}, {"first_name": "Kathleen", "last_name": "Hall", "email": "sbowman@example.com"}, {"first_name": "David", "last_name": "Hardy", "email": "wjackson@example.net"}, {"first_name": "Lisa", "last_name": "Hardy", "email": "vbaldwin@example.org"}, {"first_name": "Kathleen", "last_name": "Harrington", "email": "brownalexandra@example.com"}, {"first_name": "Jessica", "last_name": "Henry", "email": "zachary11@example.org"}, {"first_name": "Gregory", "last_name": "Hernandez", "email": "vjenkins@example.net"}, {"first_name": "John", "last_name": "Hernandez", "email": "vcameron@example.org"}, {"first_name": "James", "last_name": "Huang", "email": "eparker@example.net"}, {"first_name": "Jennifer", "last_name": "Hubbard", "email": "nbrown@example.net"}, {"first_name": "Joshua", "last_name": "Huerta", "email": "tamara54@example.net"}, {"first_name": "David", "last_name": "Jackson", "email": "rachelwood@example.org"}, {"first_name": "Nicole", "last_name": "Jennings", "email": "nguyengary@example.org"}, {"first_name": "Reginald", "last_name": "Jones", "email": "aedwards@example.org"}, {"first_name": "Jerry", "last_name": "Jordan", "email": "qmorgan@example.net"}, {"first_name": "Marcia", "last_name": "Kemp", "email": "bentleymelissa@example.com"}, {"first_name": "Bryan", "last_name": "Krueger", "email": "gedwards@example.org"}, {"first_name": "Regina", "last_name": "Lawson", "email": "pallen@example.org"}, {"first_name": "Becky", "last_name": "Lee", "email": "catherinecampbell@example.com"}, {"first_name": "Marissa", "last_name": "Lewis", "email": "pmiller@example.net"}, {"first_name": "Mark", "last_name": "Lewis", "email": "kristinlynn@example.net"}, {"first_name": "James", "last_name": "Li", "email": "aaronjackson@example.net"}, {"first_name": "Tiffany", "last_name": "Lopez", "email": "harrisbriana@example.com"}, {"first_name": "Angela", "last_name": "Lucas", "email": "luke05@example.com"}, {"first_name": "Amanda", "last_name": "Mason", "email": "clarkbrandon@example.com"}, {"first_name": "Matthew", "last_name": "Mayo", "email": "amullen@example.net"}, {"first_name": "Tammy", "last_name": "Mcgrath", "email": "lauraolson@example.org"}, {"first_name": "Shelley", "last_name": "Mitchell", "email": "xperez@example.com"}, {"first_name": "Karen", "last_name": "Moran", "email": "cynthiamorrison@example.com"}, {"first_name": "Christy", "last_name": "Morrison", "email": "angela11@example.net"}, {"first_name": "Jeffrey", "last_name": "Mullen", "email": "lanejason@example.net"}, {"first_name": "Larry", "last_name": "Norris", "email": "phillip89@example.com"}, {"first_name": "Michael", "last_name": "Oliver", "email": "aprilbrown@example.net"}, {"first_name": "Monica", "last_name": "Olson", "email": "caseynancy@example.com"}, {"first_name": "Nancy", "last_name": "Ortiz", "email": "melendezchristopher@example.org"}, {"first_name": "Benjamin", "last_name": "Owens", "email": "markjohnson@example.org"}, {"first_name": "Edward", "last_name": "Park", "email": "jennifer44@example.com"}, {"first_name": "Edward", "last_name": "Patton", "email": "monica48@example.org"}, {"first_name": "Timothy", "last_name": "Pittman", "email": "josephmurillo@example.com"}, {"first_name": "Gina", "last_name": "Powers", "email": "stephanie45@example.org"}, {"first_name": "Kara", "last_name": "Ramirez", "email": "frankpugh@example.com"}, {"first_name": "Sabrina", "last_name": "Ramirez", "email": "susanchavez@example.org"}, {"first_name": "Bill", "last_name": "Reed", "email": "zpatel@example.com"}, {"first_name": "Kevin", "last_name": "Reynolds", "email": "roger56@example.net"}, {"first_name": "Paul", "last_name": "Rice", "email": "jennahill@example.com"}, {"first_name": "Amanda", "last_name": "Riley", "email": "donna65@example.com"}, {"first_name": "Heather", "last_name": "Robinson", "email": "zhowell@example.com"}, {"first_name": "Heather", "last_name": "Romero", "email": "wgordon@example.org"}, {"first_name": "Justin", "last_name": "Ruiz", "email": "patricia84@example.net"}, {"first_name": "Dana", "last_name": "Savage", "email": "martinkimberly@example.org"}, {"first_name": "Heather", "last_name": "Sims", "email": "david14@example.org"}, {"first_name": "Jeffrey", "last_name": "Smith", "email": "lee75@example.net"}, {"first_name": "Megan", "last_name": "Stevens", "email": "davismichelle@example.org"}, {"first_name": "Lisa", "last_name": "Tanner", "email": "josephgreen@example.com"}, {"first_name": "Deborah", "last_name": "Tate", "email": "abennett@example.net"}, {"first_name": "Hannah", "last_name": "Taylor", "email": "klee@example.net"}, {"first_name": "Terri", "last_name": "Taylor", "email": "prestongary@example.com"}, {"first_name": "Crystal", "last_name": "Terry", "email": "carrerika@example.net"}, {"first_name": "David", "last_name": "Thomas", "email": "stephanie52@example.com"}, {"first_name": "Kenneth", "last_name": "Valdez", "email": "dunnkaitlin@example.com"}, {"first_name": "Amy", "last_name": "Walker", "email": "adamsutton@example.com"}, {"first_name": "Stephen", "last_name": "Wall", "email": "phillipsmelissa@example.net"}, {"first_name": "Kevin", "last_name": "Waller", "email": "qvaughn@example.org"}, {"first_name": "Diane", "last_name": "Williams", "email": "hmack@example.org"}, {"first_name": "Andrea", "last_name": "Wu", "email": "tschultz@example.com"}]
# for a1, b1 in zip(a, b):
#     if a1 != b1:
#         print(a1, b1)
#         break
# from datagen import (
#     get_markdown,
#     get_dates,
#     get_contacts,
#     get_logs,
#     get_docs,
#     get_email,
#     get_credit_card,
#     get_comments,
#     get_tickets,
# )
# def a2(email: str, file: str = "/data/format.md", **kwargs):
#     original = get_markdown(email)
#     subprocess.run(["npx","--version"])
#     try:
#         result = subprocess.run(
#             ["npx", "prettier@3.4.2", "--stdin-filepath", file],
#             input=original,
#             capture_output=True,
#             text=True,
#             check=True,
#             # Ensure npx is picked up from the PATH on Windows
#             #shell=True,
#         )
#         expected = result.stdout
#     except subprocess.CalledProcessError as e:
#         print(f"Error running prettier: {e}")
#         return None
#     return expected

# print(a2("23f1002382@ds.study.iitm.ac.in", "/data/format.md"))

# from ollama import chat
# from ollama import ChatResponse

# # response = chat(model='qwen2.5:3b', messages=[
# #   {
# #     'role': 'user',
# #     'content': 'Hello',
# #   },
# # ])
# # print(response.message.content)
# response = chat(
#             'qwen2.5:3b',
#             messages=[ {'role': 'system','content': 'extract the senders email address.YOUR response should be only the email address.'},
#                         {'role': 'user', 'content': """From: John Doe <johndoe@example.com>
# To: Jane Smith <janesmith@example.com>
# Subject: Important Meeting Update
# Date: Mon, 12 Feb 2024 10:15:30 -0500
# Message-ID: <f4e3a2b1-5678-9876-abcd-1234567890ef@example.com>

# Dear Jane,

# I hope you're doing well. I wanted to update you regarding our upcoming meeting scheduled for Wednesday at 3 PM. We will be discussing the latest project developments and upcoming deadlines.

# Please let me know if this time works for you or if you’d like to reschedule.

# Looking forward to our discussion.

# Best regards,  
# John Doe  
# Senior Project Manager  
# Example Corp  """}])
# print(response.message.content)
result = {
  "building/garden.md": "Wind address I official answer.",
  "building/growth.md": "Instead consumer yourself who.",
  "building/gun.md": "Control woman every forward traditional hear measure.",
  "building/high.md": "Stage program side.",
  "building/including.md": "Value student five.",
  "building/main.md": "Past news way.",
  "building/pass.md": "Teacher he blue property visit value energy.",
  "building/person.md": "Executive interest wide collection office center seek.",
  "building/road.md": "Sometimes wrong brother computer girl eye.",
  "building/wrong.md": "Teacher against probably study to Mrs.",
  "child/common.md": "Important realize cost.",
  "child/decide.md": "Discover bank population form cultural offer.",
  "child/drop.md": "Line provide main morning use program.",
  "child/forget.md": "Local religious amount.",
  "child/gas.md": "Consider skin great much full dream.",
  "child/ground.md": "Sometimes country them stock officer.",
  "child/lot.md": "Structure model as network.",
  "child/play.md": "Suggest technology music run worker statement.",
  "child/take.md": "Car measure too.",
  "child/that.md": "System open someone trip practice purpose think.",
  "expert/cover.md": "Them entire culture firm evening play material.",
  "expert/decision.md": "Picture something service seat.",
  "expert/figure.md": "Coach standard position lawyer that everybody.",
  "expert/grow.md": "Month peace remain place.",
  "expert/indicate.md": "Ever white rule trade old.",
  "expert/never.md": "Series cost people get present speech firm.",
  "expert/no.md": "Describe place poor want increase according wrong.",
  "expert/toward.md": "Ever hit structure early opportunity impact.",
  "expert/treat.md": "Tend trial suddenly on possible event.",
  "expert/trip.md": "Whatever reduce avoid indeed rest improve.",
  "fund/any.md": "What on leader pressure.",
  "fund/carry.md": "Stop Democrat where professional.",
  "fund/fight.md": "Against management could skin image trial to.",
  "fund/leave.md": "Early quite sell return mention budget.",
  "fund/minute.md": "Civil statement good particular.",
  "fund/production.md": "She few must Democrat season cut.",
  "fund/school.md": "Environment beat certainly five quite.",
  "fund/shake.md": "Wrong hand power.",
  "fund/white.md": "Figure woman quality once support usually reveal.",
  "fund/woman.md": "Congress while so collection decision whole energy.",
  "possible/brother.md": "Deep office thought official.",
  "possible/culture.md": "Kid cell around science southern southern truth.",
  "possible/far.md": "Sure long late upon job about.",
  "possible/he.md": "Seem feeling car west edge assume.",
  "possible/kid.md": "My mission somebody ago.",
  "possible/miss.md": "Despite set church white former.",
  "possible/series.md": "Indicate charge any itself send.",
  "possible/that.md": "Everything certainly attorney their.",
  "possible/wife.md": "Seven behind notice whose see unit.",
  "possible/yes.md": "Pressure some growth build.",
  "product/bar.md": "Treatment fly either.",
  "product/cup.md": "Strategy direction cause herself.",
  "product/in.md": "Husband keep individual beyond change company get laugh.",
  "product/issue.md": "Early theory team discover international goal.",
  "product/media.md": "Until thing peace suggest meeting upon west.",
  "product/plan.md": "American commercial activity rest fire oil.",
  "product/road.md": "Office central drive finally have.",
  "product/suffer.md": "Particularly design discussion tend smile.",
  "product/those.md": "Blood building affect space concern hour.",
  "product/worry.md": "Drive mouth peace professional either culture.",
  "represent/along.md": "This seven open cold.",
  "represent/article.md": "Focus natural control know buy effort.",
  "represent/big.md": "Black short rock executive ten effort beat.",
  "represent/center.md": "Difficult boy although successful nice against food.",
  "represent/financial.md": "Three instead evening star relate.",
  "represent/focus.md": "Book start which involve bad.",
  "represent/maybe.md": "Cold level follow office professor.",
  "represent/open.md": "Region situation modern most speech.",
  "represent/produce.md": "Account fast dream live because.",
  "represent/sea.md": "Human strategy foot safe eight play back two.",
  "teach/again.md": "Red more young style too treat history.",
  "teach/city.md": "Nature wind market outside those.",
  "teach/help.md": "Position song foreign under over her.",
  "teach/late.md": "Art opportunity mission west set detail hair.",
  "teach/notice.md": "Strategy seat provide late toward.",
  "teach/physical.md": "Stock contain wish article.",
  "teach/recognize.md": "Billion woman both performance.",
  "teach/responsibility.md": "North learn source health.",
  "teach/team.md": "Reveal program Mr yes.",
  "teach/then.md": "Fill leave understand fly thank environmental.",
  "trade/able.md": "Try art catch stop.",
  "trade/court.md": "Memory note give or analysis bar happy.",
  "trade/finally.md": "Finally Mrs arm conference face billion.",
  "trade/nature.md": "Operation about prevent movie south over.",
  "trade/purpose.md": "Clear nearly character just run.",
  "trade/start.md": "From police up matter town.",
  "trade/suffer.md": "Skill second like baby mouth artist.",
  "trade/technology.md": "Really professional thousand nearly inside wait.",
  "trade/than.md": "Chair author appear concern.",
  "trade/turn.md": "Our step figure.",
  "whose/after.md": "Quickly born matter.",
  "whose/begin.md": "Push hair view person.",
  "whose/debate.md": "Of money beyond though might.",
  "whose/girl.md": "Professor respond detail song.",
  "whose/light.md": "Treatment in sometimes significant maybe sense.",
  "whose/nature.md": "Middle social summer property song body break.",
  "whose/newspaper.md": "That study general couple.",
  "whose/nice.md": "Buy people forget truth trade this.",
  "whose/station.md": "We identify least what.",
  "whose/two.md": "Stock last part."
}
expected = {'whose/nature.md': 'Middle social summer property song body break.', 
'whose/station.md': 'We identify least what.', 
'whose/newspaper.md': 'That study general couple.', 'whose/debate.md': 'Of money beyond though might.', 'whose/light.md': 'Treatment in sometimes significant maybe sense.', 'whose/begin.md': 'Push hair view person.', 'whose/nice.md': 'Buy people forget truth trade this.', 'whose/after.md': 'Quickly born matter.', 'whose/girl.md': 'Professor respond detail song.', 'whose/two.md': 'Stock last part.', 'building/garden.md': 'Wind address I official answer.', 'building/including.md': 'Value student five.', 'building/gun.md': 'Control woman every forward traditional hear measure.', 'building/high.md': 'Stage program side.', 'building/main.md': 'Past news way.', 'building/person.md': 'Executive interest wide collection office center seek.', 'building/road.md': 'Sometimes wrong brother computer girl eye.', 'building/pass.md': 'Teacher he blue property visit value energy.', 'building/wrong.md': 'Teacher against probably study to Mrs.', 'building/growth.md': 'Instead consumer yourself who.', 'child/lot.md': 'Structure model as network.', 'child/gas.md': 'Consider skin great much full dream.', 'child/that.md': 'System open someone trip practice purpose think.', 'child/drop.md': 'Line provide main morning use program.', 'child/forget.md': 'Local religious amount.', 'child/decide.md': 'Discover bank population form cultural offer.', 'child/common.md': 'Important realize cost.', 'child/ground.md': 'Sometimes country them stock officer.', 'child/play.md': 'Suggest technology music run worker statement.', 'child/take.md': 'Car measure too.', 'possible/brother.md': 'Deep office thought official.', 'possible/culture.md': 'Kid cell around science southern southern truth.', 'possible/kid.md': 'My mission somebody ago.', 'possible/he.md': 'Seem feeling car west edge assume.', 'possible/far.md': 'Sure long late upon job about.', 'possible/wife.md': 'Seven behind notice whose see unit.', 'possible/miss.md': 'Despite set church white former.', 'possible/series.md': 'Indicate charge any itself send.', 'possible/that.md': 'Everything certainly attorney their.', 'possible/yes.md': 'Pressure some growth build.', 'product/worry.md': 'Drive mouth peace professional either culture.', 'product/bar.md': 'Treatment fly either.', 'product/plan.md': 'American commercial activity rest fire oil.', 'product/issue.md': 'Early theory team discover international goal.', 'product/those.md': 'Blood building affect space concern hour.', 'product/media.md': 'Until thing peace suggest meeting upon west.', 'product/in.md': 'Husband keep individual beyond change company get laugh.', 'product/suffer.md': 'Particularly design discussion tend smile.', 'product/cup.md': 'Strategy direction cause herself.', 'product/road.md': 'Office central drive finally have.', 'fund/woman.md': 'Congress while so collection decision whole energy.', 'fund/fight.md': 'Against management could skin image trial to.', 'fund/white.md': 'Figure woman quality once support usually reveal.', 'fund/school.md': 'Environment beat certainly five quite.', 'fund/any.md': 'What on leader pressure.', 'fund/leave.md': 'Early quite sell return mention budget.', 'fund/minute.md': 'Civil statement good particular.', 'fund/production.md': 'She few must Democrat season cut.', 'fund/shake.md': 'Wrong hand power.', 'fund/carry.md': 'Stop Democrat where professional.', 'teach/then.md': 'Fill leave understand fly thank environmental.', 'teach/team.md': 'Reveal program Mr yes.', 'teach/recognize.md': 'Billion woman both performance.', 'teach/help.md': 'Position song foreign under over her.', 'teach/notice.md': 'Strategy seat provide late toward.', 'teach/city.md': 'Nature wind market outside those.', 'teach/again.md': 'Red more young style too treat history.', 'teach/late.md': 'Art opportunity mission west set detail hair.', 'teach/physical.md': 'Stock contain wish article.', 'teach/responsibility.md': 'North learn source health.', 'trade/start.md': 'From police up matter town.', 'trade/court.md': 'Memory note give or analysis bar happy.', 'trade/able.md': 'Try art catch stop.', 'trade/purpose.md': 'Clear nearly character just run.', 'trade/than.md': 'Chair author appear concern.', 'trade/finally.md': 'Finally Mrs arm conference face billion.', 'trade/nature.md': 'Operation about prevent movie south over.', 'trade/suffer.md': 'Skill second like baby mouth artist.', 'trade/technology.md': 'Really professional thousand nearly inside wait.', 'trade/turn.md': 'Our step figure.', 'expert/cover.md': 'Them entire culture firm evening play material.', 'expert/decision.md': 'Picture something service seat.', 'expert/toward.md': 'Ever hit structure early opportunity impact.', 'expert/figure.md': 'Coach standard position lawyer that everybody.', 'expert/indicate.md': 'Ever white rule trade old.', 'expert/never.md': 'Series cost people get present speech firm.', 'expert/no.md': 'Describe place poor want increase according wrong.', 'expert/treat.md': 'Tend trial suddenly on possible event.', 'expert/trip.md': 'Whatever reduce avoid indeed rest improve.', 'expert/grow.md': 'Month peace remain place.', 'represent/maybe.md': 'Cold level follow office professor.', 'represent/big.md': 'Black short rock executive ten effort beat.', 'represent/along.md': 'This seven open cold.', 'represent/article.md': 'Focus natural control know buy effort.', 'represent/focus.md': 'Book start which involve bad.', 'represent/financial.md': 'Three instead evening star relate.', 'represent/center.md': 'Difficult boy although successful nice against food.', 'represent/produce.md': 'Account fast dream live because.', 'represent/sea.md': 'Human strategy foot safe eight play back two.', 'represent/open.md': 'Region situation modern most speech.'}
print(len(result), len(expected))
count = 0
for x in result:
    for y in expected:
        if x == y:
            if result[x] != expected[y]:
                count += 1
                print(f"{x}:{result[x]} ----- {y}:{result[y]}")
                print(count)
                break
