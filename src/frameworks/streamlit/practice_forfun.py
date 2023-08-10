import streamlit as st
from os import getcwd
from practice_forfun_helpers import create_object, load_duckdb_table, create_duckdb_sql_table, df_to_data_list, render_image

# Load the table
infos_df = load_duckdb_table('infos')

# Hard-coded Data
# data = [
#     create_object('John', '12345', 'New York', f'{getcwd()}/new-york-new-york-city.gif'),
#     create_object('Emma', 'abc123', 'London', f'{getcwd()}/fb95eca49cf3f2af57455b1358f1ec39193ce256.webp'),
#     create_object('Tom', 'abcd', 'Paris', f'{getcwd()}/france-eiffel-tower-paris.jpg')
# ]

# create_duckdb_sql_table(data)

# Create the data list
data = df_to_data_list(infos_df)
# for i in range(len(data)):
#     print(data[i]['username'])
col1, col2 = st.columns(2)

# def check_username(username):
#     for i in range(len(data)):
#         if username in data[i].values:
#             return True
#         else:
#             return False

def check_username(username):
    return username in [user['username'] for user in data]

def main():  
    # Ask for username input         
    username = st.text_input("Enter a username:")
 
    if st.button("Check"):
        if username:
            if check_username(username):
                st.write("Username already exists in the dataset. Please try again.")
            else:
                st.empty() #Clear the previous inputs
                st.write("Username does not exist in the dataset.")

                password = st.text_input("Enter a password:")

                if st.button('Register'):
                    # Add to the data list
                    new_result = create_object(username, password, 'NULL', 'NULL')
                    data.append(new_result)
                    # Add to the DuckDB SQL table
                    create_duckdb_sql_table(data)


                
if __name__ == '__main__':
    main()
    # Loop through each data object
    for obj in data:
        st.markdown("<h3>username: </h3>", unsafe_allow_html=True)
        username = st.markdown(obj['username'], unsafe_allow_html=True)
        
        st.markdown("<h3>password: </h3>", unsafe_allow_html=True)
        password = st.markdown(obj['password'], unsafe_allow_html=True)
        
        st.markdown("<h3>bio: </h3>", unsafe_allow_html=True)
        age = st.markdown(obj['bio'], unsafe_allow_html=True)

        #area = st.markdown(obj['image'], unsafe_allow_html=True)
        #left_column,right_column=st.columns(2)

# Button 1 in the first column
# i=0
# if col1.button('Sign Up'):
#   while i == 0:
#       user_name = st.text_input("Username: ", key=input_key)
#       #password = st.text_input("Password: ")
#       if user_name in data[0]:
#            i==0
#       else:
#            i==1



# # Button 2 in the second column
# if col2.button('Login'):
#      st.write('Button 2 was clicked!')