import streamlit as st

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Polyhouse Calculator", "Column Calculation"]
)

if page == "Polyhouse Calculator":
    # ... your Polyhouse Calculator code (as before) 
    polyhouse_type = st.selectbox('Select type of polyhouse:', ['', 'NVPH', 'Net House', 'Fan and Pad'])

    if polyhouse_type == 'NVPH':
        road = st.selectbox('Road Inside:', ['', 'Present', 'Absent'])
        bay_size = st.text_input('Bay size:')
        hockey_space = st.number_input('Hockey space:')
        type_of_structure = st.selectbox('Type of structure:', ['', 'Stepper', 'Symmetric'])

        domes_list = []
        no_of_steps = None
        isstepper=False
        single_domes=0
        
        # Only show stepper fields if chosen
        if type_of_structure == 'Stepper':
            isstepper=True
            no_of_steps = st.number_input('Number of steps:', min_value=0, step=1, value=1)
            if no_of_steps == 0:
                single_domes = st.number_input('Enter the number of domes:', min_value=0, step=1, value=0)
            else:
                for i in range(int(no_of_steps)):
                    domes = st.number_input(
                        f'Number of domes for step {i+1}:',
                        min_value=1,
                        step=1,
                        key=f'domes_{i}'
                    )
                    domes_list.append(domes)

            
    

        # Calculate button and validation
        if st.button("Calculate"):
            missing_fields = []

            if road == '':
                missing_fields.append("Road")
            if not bay_size.strip():
                missing_fields.append("Bay size")
            if (hockey_space==0.00):
                missing_fields.append("Hockey space")
            if type_of_structure == '':
                missing_fields.append("Type of structure")
            if type_of_structure == 'Stepper':
                    if(isstepper):
                        if(no_of_steps==0 and single_domes==0):
                            missing_fields.append("Number of domes")
                    for idx, domes in enumerate(domes_list):
                        if domes < 1:
                            missing_fields.append(f"Number of domes for step {idx+1}")

            if missing_fields:
                st.error("Please enter all required fields:\n- " + "\n- ".join(missing_fields))
            else:
                # Example calculation
                if type_of_structure == 'Stepper':
                    total_domes = sum(domes_list)+single_domes
                    st.success(f"Total number of domes: {total_domes}")
                else:
                    st.success("All fields are filled! (No calculation for symmetric structure in this example)")


    elif polyhouse_type=='Net House':
        road = st.selectbox('Road Inside:', ['', 'Present', 'Absent'])
        bay_size = st.text_input('Bay size:')
        hockey_space = st.text_input('Hockey space:')
        type_of_structure = st.selectbox('Type of structure:', ['', 'Stepper', 'Symmetric'])

        domes_list = []
        no_of_steps = None

        # Only show stepper fields if chosen
        if type_of_structure == 'Stepper':
            no_of_steps = st.number_input('Number of steps:', min_value=0, step=1, value=1)
            if(no_of_steps==0):
                domes=st.number_input(
                    f'Enter the number of domes:',min_value=0,step=1,value=1
                )
                domes_list.append(domes)
            else:
                for i in range(int(no_of_steps)):
                    domes = st.number_input(
                    f'Number of domes for step {i+1}:',
                    min_value=1,  # Set min_value=1 to require input
                    step=1,
                    key=f'domes_{i}'
                )
                    domes_list.append(domes)

            
    

        # Calculate button and validation
        if st.button("Calculate"):
            missing_fields = []

            if road == '':
                missing_fields.append("Road")
            if not bay_size.strip():
                missing_fields.append("Bay size")
            if not hockey_space.strip():
                missing_fields.append("Hockey space")
            if type_of_structure == '':
                missing_fields.append("Type of structure")
            if type_of_structure == 'Stepper':
                if not no_of_steps or no_of_steps < 1:
                    missing_fields.append("Number of steps")
                for idx, domes in enumerate(domes_list):
                    if domes < 1:
                        missing_fields.append(f"Number of domes for step {idx+1}")

            if missing_fields:
                st.error("Please enter all required fields:\n- " + "\n- ".join(missing_fields))
            else:
                # Example calculation
                if type_of_structure == 'Stepper':
                    total_domes = sum(domes_list)
                    st.success(f"Total number of domes: {total_domes}")
                else:
                    st.success("All fields are filled! (No calculation for symmetric structure in this example)")


    elif polyhouse_type in ['Net House', 'Fan and Pad']:
        st.info(f"You selected '{polyhouse_type}'. No further inputs required for this type.")

    elif polyhouse_type == '':
        st.info("Please select the type of polyhouse to proceed.")

elif page == "Column Calculation":
    # Step 1: Polyhouse type selection
    polyhouse_type = st.selectbox('Select type of polyhouse:', ['', 'NVPH', 'Net House', 'Fan and Pad'])

    if polyhouse_type == 'NVPH':
        road = st.selectbox('Road Inside:', ['', 'Present', 'Absent'])
        bay_size = st.text_input('Bay size:')
        hockey_space = st.number_input('Hockey space:')
        type_of_structure = st.selectbox('Type of structure:', ['', 'Stepper', 'Symmetric'])

        dome_data = []  # Will store [number_of_domes, length] for each step
        no_of_steps = None
        single_domes = 0
        single_length = 0.0

        if type_of_structure == 'Stepper':
            no_of_steps = st.number_input('Number of steps:', min_value=0, step=1, value=1)
            if no_of_steps == 0:
                single_domes = st.number_input('Enter the number of domes:', min_value=1, step=1, value=1)
                single_length = st.number_input('Enter the length of dome:', min_value=0.0, step=0.1, value=0.0)
            else:
                for i in range(int(no_of_steps)):
                    domes = st.number_input(
                        f'Number of domes for step {i+1}:',
                        min_value=1,
                        step=1,
                        key=f'domes_{i}'
                    )
                    length = st.number_input(
                        f'Length of domes for step {i+1}:',
                        min_value=0.0,
                        step=0.1,
                        key=f'length_{i}'
                    )
                    dome_data.append([domes, length])

        # Calculate button and validation
        if st.button("Calculate"):
            missing_fields = []

            if road == '':
                missing_fields.append("Road")
            if not bay_size.strip():
                missing_fields.append("Bay size")
            if (hockey_space==0.00):
                missing_fields.append("Hockey space")
            if type_of_structure == '':
                missing_fields.append("Type of structure")
            if type_of_structure == 'Stepper':
                if no_of_steps is None:
                    missing_fields.append("Number of steps")
                elif no_of_steps == 0:
                    if single_domes < 1:
                        missing_fields.append("Number of domes")
                    if single_length <= 0:
                        missing_fields.append("Length of dome")
                else:
                    for idx, (domes, length) in enumerate(dome_data):
                        if domes < 1:
                            missing_fields.append(f"Number of domes for step {idx+1}")
                        if length <= 0:
                            missing_fields.append(f"Length of domes for step {idx+1}")

            if missing_fields:
                st.error("Please enter all required fields:\n- " + "\n- ".join(missing_fields))
            else:
                # Example calculation: total domes and lengths
                if type_of_structure == 'Stepper':
                    if no_of_steps == 0:
                        st.success(f"Number of domes: {single_domes}, Length: {single_length}")
                    else:
                        total_domes = sum([d[0] for d in dome_data])
                        # total_columns = sum([d[0]*d[1]/4 for d in dome_data])
                        total_columns=0
                        for i in range(len(dome_data)):
                            total_columns+=dome_data[i][0]*(dome_data[i][1]-2*hockey_space)/4    
                        total_columns+=(dome_data[len(dome_data)-1][1]-2*hockey_space)/4
                        st.success(f"Total number of domes: {total_domes}, Total columns: {total_columns}")
                else:
                    st.success("All fields are filled! (No calculation for symmetric structure in this example)")

    # Repeat similar logic for Net House if needed...

elif page == "Home":
    st.write("This is to be handled next.")
