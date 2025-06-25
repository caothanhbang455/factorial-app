import streamlit as st
from factorial import fact

# st.title("Application for basic calculations")

# st.header("Find factorial of a number n")

# st.write("This application allows users to calculate a factorial of a number" \
# " please input a number and press button 'Calcualte'")

def main():

    st.title("Factorial Caculator")

    n = st.number_input("Enter a number:", min_value = 0, max_value=999)

    if st.button("Caculate"):
        result = fact(n)
        st.write(f'The factorial of {n} is {result}')

if __name__ == '__main__':
    main()