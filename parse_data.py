import json
#JSON Parsing
def parse_json_file(file_path):
    try:
        
        with open(file_path, 'r') as file:
            
            users = json.load(file)

            print(f"This is the data from our JSON file")
            for user in users:
                
                print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)

if __name__ == "__main__":
    
    json_file_path = '/home/devasc/labs/devnet-src/project1/data.json'
    parse_json_file(json_file_path)
    
import xml.etree.ElementTree as ET
#XML Parsing

def parse_xml_file(file_path):
    try:
        
        tree = ET.parse(file_path)
        root = tree.getroot()

        print(f"This is the data from our XML File")
        for user in root.findall('user'):
            user_id = user.find('id').text
            user_name = user.find('name').text
            user_email = user.find('email').text
            
          
            print(f"ID: {user_id}, Name: {user_name}, Email: {user_email}")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except ET.ParseError as e:
        print("Failed to parse XML:", e)

if __name__ == "__main__":
    
    xml_file_path = '/home/devasc/labs/devnet-src/project1/data.xml'  
    parse_xml_file(xml_file_path)
    
import yaml
#YAML Parsing

def parse_yaml_file(file_path):
    try:
        
        with open(file_path, 'r') as file:
            
            data = yaml.safe_load(file)

            print(f"This is the data from our YAML file")
            for user in data['users']:
                user_id = user['id']
                user_name = user['name']
                user_email = user['email']
                
                
                print(f"ID: {user_id}, Name: {user_name}, Email: {user_email}")

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except yaml.YAMLError as e:
        print("Failed to parse YAML:", e)

if __name__ == "__main__":
    
    yaml_file_path = '/home/devasc/labs/devnet-src/project1/data.yaml'  
    parse_yaml_file(yaml_file_path)
