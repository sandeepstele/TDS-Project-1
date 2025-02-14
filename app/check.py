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
# result = {
#   "building/garden.md": "Wind address I official answer.",
#   "building/growth.md": "Instead consumer yourself who.",
#   "building/gun.md": "Control woman every forward traditional hear measure.",
#   "building/high.md": "Stage program side.",
#   "building/including.md": "Value student five.",
#   "building/main.md": "Past news way.",
#   "building/pass.md": "Teacher he blue property visit value energy.",
#   "building/person.md": "Executive interest wide collection office center seek.",
#   "building/road.md": "Sometimes wrong brother computer girl eye.",
#   "building/wrong.md": "Teacher against probably study to Mrs.",
#   "child/common.md": "Important realize cost.",
#   "child/decide.md": "Discover bank population form cultural offer.",
#   "child/drop.md": "Line provide main morning use program.",
#   "child/forget.md": "Local religious amount.",
#   "child/gas.md": "Consider skin great much full dream.",
#   "child/ground.md": "Sometimes country them stock officer.",
#   "child/lot.md": "Structure model as network.",
#   "child/play.md": "Suggest technology music run worker statement.",
#   "child/take.md": "Car measure too.",
#   "child/that.md": "System open someone trip practice purpose think.",
#   "expert/cover.md": "Them entire culture firm evening play material.",
#   "expert/decision.md": "Picture something service seat.",
#   "expert/figure.md": "Coach standard position lawyer that everybody.",
#   "expert/grow.md": "Month peace remain place.",
#   "expert/indicate.md": "Ever white rule trade old.",
#   "expert/never.md": "Series cost people get present speech firm.",
#   "expert/no.md": "Describe place poor want increase according wrong.",
#   "expert/toward.md": "Ever hit structure early opportunity impact.",
#   "expert/treat.md": "Tend trial suddenly on possible event.",
#   "expert/trip.md": "Whatever reduce avoid indeed rest improve.",
#   "fund/any.md": "What on leader pressure.",
#   "fund/carry.md": "Stop Democrat where professional.",
#   "fund/fight.md": "Against management could skin image trial to.",
#   "fund/leave.md": "Early quite sell return mention budget.",
#   "fund/minute.md": "Civil statement good particular.",
#   "fund/production.md": "She few must Democrat season cut.",
#   "fund/school.md": "Environment beat certainly five quite.",
#   "fund/shake.md": "Wrong hand power.",
#   "fund/white.md": "Figure woman quality once support usually reveal.",
#   "fund/woman.md": "Congress while so collection decision whole energy.",
#   "possible/brother.md": "Deep office thought official.",
#   "possible/culture.md": "Kid cell around science southern southern truth.",
#   "possible/far.md": "Sure long late upon job about.",
#   "possible/he.md": "Seem feeling car west edge assume.",
#   "possible/kid.md": "My mission somebody ago.",
#   "possible/miss.md": "Despite set church white former.",
#   "possible/series.md": "Indicate charge any itself send.",
#   "possible/that.md": "Everything certainly attorney their.",
#   "possible/wife.md": "Seven behind notice whose see unit.",
#   "possible/yes.md": "Pressure some growth build.",
#   "product/bar.md": "Treatment fly either.",
#   "product/cup.md": "Strategy direction cause herself.",
#   "product/in.md": "Husband keep individual beyond change company get laugh.",
#   "product/issue.md": "Early theory team discover international goal.",
#   "product/media.md": "Until thing peace suggest meeting upon west.",
#   "product/plan.md": "American commercial activity rest fire oil.",
#   "product/road.md": "Office central drive finally have.",
#   "product/suffer.md": "Particularly design discussion tend smile.",
#   "product/those.md": "Blood building affect space concern hour.",
#   "product/worry.md": "Drive mouth peace professional either culture.",
#   "represent/along.md": "This seven open cold.",
#   "represent/article.md": "Focus natural control know buy effort.",
#   "represent/big.md": "Black short rock executive ten effort beat.",
#   "represent/center.md": "Difficult boy although successful nice against food.",
#   "represent/financial.md": "Three instead evening star relate.",
#   "represent/focus.md": "Book start which involve bad.",
#   "represent/maybe.md": "Cold level follow office professor.",
#   "represent/open.md": "Region situation modern most speech.",
#   "represent/produce.md": "Account fast dream live because.",
#   "represent/sea.md": "Human strategy foot safe eight play back two.",
#   "teach/again.md": "Red more young style too treat history.",
#   "teach/city.md": "Nature wind market outside those.",
#   "teach/help.md": "Position song foreign under over her.",
#   "teach/late.md": "Art opportunity mission west set detail hair.",
#   "teach/notice.md": "Strategy seat provide late toward.",
#   "teach/physical.md": "Stock contain wish article.",
#   "teach/recognize.md": "Billion woman both performance.",
#   "teach/responsibility.md": "North learn source health.",
#   "teach/team.md": "Reveal program Mr yes.",
#   "teach/then.md": "Fill leave understand fly thank environmental.",
#   "trade/able.md": "Try art catch stop.",
#   "trade/court.md": "Memory note give or analysis bar happy.",
#   "trade/finally.md": "Finally Mrs arm conference face billion.",
#   "trade/nature.md": "Operation about prevent movie south over.",
#   "trade/purpose.md": "Clear nearly character just run.",
#   "trade/start.md": "From police up matter town.",
#   "trade/suffer.md": "Skill second like baby mouth artist.",
#   "trade/technology.md": "Really professional thousand nearly inside wait.",
#   "trade/than.md": "Chair author appear concern.",
#   "trade/turn.md": "Our step figure.",
#   "whose/after.md": "Quickly born matter.",
#   "whose/begin.md": "Push hair view person.",
#   "whose/debate.md": "Of money beyond though might.",
#   "whose/girl.md": "Professor respond detail song.",
#   "whose/light.md": "Treatment in sometimes significant maybe sense.",
#   "whose/nature.md": "Middle social summer property song body break.",
#   "whose/newspaper.md": "That study general couple.",
#   "whose/nice.md": "Buy people forget truth trade this.",
#   "whose/station.md": "We identify least what.",
#   "whose/two.md": "Stock last part."
# }
# expected = {'whose/nature.md': 'Middle social summer property song body break.', 
# 'whose/station.md': 'We identify least what.', 
# 'whose/newspaper.md': 'That study general couple.', 'whose/debate.md': 'Of money beyond though might.', 'whose/light.md': 'Treatment in sometimes significant maybe sense.', 'whose/begin.md': 'Push hair view person.', 'whose/nice.md': 'Buy people forget truth trade this.', 'whose/after.md': 'Quickly born matter.', 'whose/girl.md': 'Professor respond detail song.', 'whose/two.md': 'Stock last part.', 'building/garden.md': 'Wind address I official answer.', 'building/including.md': 'Value student five.', 'building/gun.md': 'Control woman every forward traditional hear measure.', 'building/high.md': 'Stage program side.', 'building/main.md': 'Past news way.', 'building/person.md': 'Executive interest wide collection office center seek.', 'building/road.md': 'Sometimes wrong brother computer girl eye.', 'building/pass.md': 'Teacher he blue property visit value energy.', 'building/wrong.md': 'Teacher against probably study to Mrs.', 'building/growth.md': 'Instead consumer yourself who.', 'child/lot.md': 'Structure model as network.', 'child/gas.md': 'Consider skin great much full dream.', 'child/that.md': 'System open someone trip practice purpose think.', 'child/drop.md': 'Line provide main morning use program.', 'child/forget.md': 'Local religious amount.', 'child/decide.md': 'Discover bank population form cultural offer.', 'child/common.md': 'Important realize cost.', 'child/ground.md': 'Sometimes country them stock officer.', 'child/play.md': 'Suggest technology music run worker statement.', 'child/take.md': 'Car measure too.', 'possible/brother.md': 'Deep office thought official.', 'possible/culture.md': 'Kid cell around science southern southern truth.', 'possible/kid.md': 'My mission somebody ago.', 'possible/he.md': 'Seem feeling car west edge assume.', 'possible/far.md': 'Sure long late upon job about.', 'possible/wife.md': 'Seven behind notice whose see unit.', 'possible/miss.md': 'Despite set church white former.', 'possible/series.md': 'Indicate charge any itself send.', 'possible/that.md': 'Everything certainly attorney their.', 'possible/yes.md': 'Pressure some growth build.', 'product/worry.md': 'Drive mouth peace professional either culture.', 'product/bar.md': 'Treatment fly either.', 'product/plan.md': 'American commercial activity rest fire oil.', 'product/issue.md': 'Early theory team discover international goal.', 'product/those.md': 'Blood building affect space concern hour.', 'product/media.md': 'Until thing peace suggest meeting upon west.', 'product/in.md': 'Husband keep individual beyond change company get laugh.', 'product/suffer.md': 'Particularly design discussion tend smile.', 'product/cup.md': 'Strategy direction cause herself.', 'product/road.md': 'Office central drive finally have.', 'fund/woman.md': 'Congress while so collection decision whole energy.', 'fund/fight.md': 'Against management could skin image trial to.', 'fund/white.md': 'Figure woman quality once support usually reveal.', 'fund/school.md': 'Environment beat certainly five quite.', 'fund/any.md': 'What on leader pressure.', 'fund/leave.md': 'Early quite sell return mention budget.', 'fund/minute.md': 'Civil statement good particular.', 'fund/production.md': 'She few must Democrat season cut.', 'fund/shake.md': 'Wrong hand power.', 'fund/carry.md': 'Stop Democrat where professional.', 'teach/then.md': 'Fill leave understand fly thank environmental.', 'teach/team.md': 'Reveal program Mr yes.', 'teach/recognize.md': 'Billion woman both performance.', 'teach/help.md': 'Position song foreign under over her.', 'teach/notice.md': 'Strategy seat provide late toward.', 'teach/city.md': 'Nature wind market outside those.', 'teach/again.md': 'Red more young style too treat history.', 'teach/late.md': 'Art opportunity mission west set detail hair.', 'teach/physical.md': 'Stock contain wish article.', 'teach/responsibility.md': 'North learn source health.', 'trade/start.md': 'From police up matter town.', 'trade/court.md': 'Memory note give or analysis bar happy.', 'trade/able.md': 'Try art catch stop.', 'trade/purpose.md': 'Clear nearly character just run.', 'trade/than.md': 'Chair author appear concern.', 'trade/finally.md': 'Finally Mrs arm conference face billion.', 'trade/nature.md': 'Operation about prevent movie south over.', 'trade/suffer.md': 'Skill second like baby mouth artist.', 'trade/technology.md': 'Really professional thousand nearly inside wait.', 'trade/turn.md': 'Our step figure.', 'expert/cover.md': 'Them entire culture firm evening play material.', 'expert/decision.md': 'Picture something service seat.', 'expert/toward.md': 'Ever hit structure early opportunity impact.', 'expert/figure.md': 'Coach standard position lawyer that everybody.', 'expert/indicate.md': 'Ever white rule trade old.', 'expert/never.md': 'Series cost people get present speech firm.', 'expert/no.md': 'Describe place poor want increase according wrong.', 'expert/treat.md': 'Tend trial suddenly on possible event.', 'expert/trip.md': 'Whatever reduce avoid indeed rest improve.', 'expert/grow.md': 'Month peace remain place.', 'represent/maybe.md': 'Cold level follow office professor.', 'represent/big.md': 'Black short rock executive ten effort beat.', 'represent/along.md': 'This seven open cold.', 'represent/article.md': 'Focus natural control know buy effort.', 'represent/focus.md': 'Book start which involve bad.', 'represent/financial.md': 'Three instead evening star relate.', 'represent/center.md': 'Difficult boy although successful nice against food.', 'represent/produce.md': 'Account fast dream live because.', 'represent/sea.md': 'Human strategy foot safe eight play back two.', 'represent/open.md': 'Region situation modern most speech.'}
# print(len(result), len(expected))

# expected = {'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}
# result  = {'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}
# print(len(set(result)), len(set(expected)))
# count = 0
# print("length of result", len(result))
# print("length of expected", len(expected))
# for y in result:
#     if y not in expected:
#         count += 1
#         print(f"{y}:{result[y]} IS EXTRA FILE")
#         print(count)
# for x in expected:
#     for y in result:
#         if x == y:
#             if result[x] != expected[y]:
#                 count += 1
#                 print(f"{x}:{result[x]} ----- {y}:{result[y]}")
#                 print(count)
#                 break
#         if y not in expected:
#             count += 1
#             print(f"{y}:{result[y]} IS EXTRA FILE")
#             print(count)
#             break

# import ollama
# import chromadb
# with open("task_to_embed.txt", "r") as file:
#    comments = file.readlines()
# documents = [comment.strip() for comment in comments]
# import numpy as np
# client = chromadb.Client()
# collection = client.create_collection(name="docs")
# for i, d in enumerate(documents):
#   response = ollama.embed(model="nomic-embed-text:latest", input=d)
#   embeddings = response["embeddings"]
#   collection.add(
#     ids=[str(i)],
#     embeddings=embeddings,
#     documents=[d]
#   )
# response = ollama.embed(model="nomic-embed-text:latest", input=documents)
# task = " /data/email.txt contains an email message. Pass the content to an LLM with instructions to extract the sender's email address, and write just the email address to /data/email-sender.txt"
#   # an example input
# print(len(response["embeddings"]))

# # generate an embedding for the input and retrieve the most relevant doc
# response = ollama.embed(
#   model="nomic-embed-text:latest",
#   input=task
# )
# results = collection.query(
#   query_embeddings=response["embeddings"][0],
#   n_results=1
# )
# data = results['documents'][0][0]
# print(data)
# print("Embedding size: ", len(response["embeddings"][0]))
# print(response)
# import base64
# image_path = "TDS_wk3_q4.png"
# with open(image_path, "rb") as file:
#   image_data = base64.b64encode(file.read()).decode("utf-8")
# print(image_data)
import dotenv
dotenv.load_dotenv()
API_KEY = os.getenv("OPEN_AI_PROXY_TOKEN")
URL_CHAT = os.getenv("OPEN_AI_PROXY_URL")
URL_EMBEDDING = os.getenv("OPEN_AI_EMBEDDING_URL")
import requests
import base64
def query_gpt_image(image_path: str, task: str):
    print("🔍 Image Path:", image_path)
    image_format = image_path.split(".")[-1]
    with open(image_path, "rb") as file:
        base64_image = base64.b64encode(file.read()).decode("utf-8")
    response = requests.post(
        URL_CHAT,
        headers={"Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{'role': 'system','content':"JUST GIVE the required input, as short as possible, one word if possible"},
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": task},
                    {
                    "type": "image_url",
                    "image_url": { "url": f"data:image/{image_format};base64,{base64_image}" }
                    }
                ]
                }
            ]
            }
                     )

    response.raise_for_status()
    result = response.json() 
    print(response)
    print(response.json())
    result = response.json() 
    return result
response = query_gpt_image("data/credit_card.png","Extract number from image")
try:
    print(response[])

# def a9(email):
#     from datagen import get_comments
#     data = get_comments(email)  
#     response = requests.post(
#                 URL_EMBEDDING,
#                 headers={"Authorization": f"Bearer {API_KEY}"},
#                 json={"model": "text-embedding-3-small", "input": data},
#             )
#     return response.json()
# print(a9("23f1002382@ds.study.iitm.ac.in"))