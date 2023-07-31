import streamlit as st

# Create a dictionary of choices
choice_dict = {'less than': '$lt',
                'less than or equal to': '$lte',
                'greater than': '$gt',
                'greater than or equal to' : '$gte',
                'equal to' : '$eq',
                'not equal to': '$ne'
                }

def value_selection(num, choice):
 
    if choice in choice_dict:
        selected_choice = {choice_dict[choice] : num}

        # # If selected choice equal to, switch to num
        # if choice_dict[choice] is None:
        #     selected_choice = num

    return selected_choice
    
class NumberDropdown:
    def __init__(self, docs: list, key: str, id: int):
        self.docs = docs
        self.column = key
        self.id = id
    
    def create_dropdown(self, collector: list):
        # Setup Markdown
        st.markdown(f"<h3 style='text-align:center'> Options for {self.column} </h3>", unsafe_allow_html=True)

        # Unique values for the key
        unique_values = list(set([doc[self.column] for doc in self.docs]))

        # Set minimum value
        arg_min = min(unique_values)

        # Set max
        arg_max = max(unique_values)

        # Get the choice
        self.choice = st.selectbox(f"Choose an option for how you want your number query for column: {self.column}",
                                   options=list(choice_dict.keys()), key=f"dropdown_{self.id}")

        # Create a dropdown
        self.dropdown = st.number_input(f"Select an option for column: {self.column}:", min_value=arg_min, max_value=arg_max, key=f"number_{self.id}")

        collector.append({self.column : value_selection(self.dropdown, self.choice)})

