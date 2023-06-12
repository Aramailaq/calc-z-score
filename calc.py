import streamlit as st
import math

def calculate_probability(mean, std_dev, x_value):
    z_score = (x_value - mean) / std_dev
    probability = 0.5 * (1 + math.erf(z_score / math.sqrt(2)))
    return probability

def main():
    st.title('Normal Distribution Calculator')

    mean = st.number_input('Mean')
    std_dev = st.number_input('Standard Deviation')
    x_value = st.number_input('X-Value')

    if st.button('Calculate'):
        probability = calculate_probability(mean, std_dev, x_value)
        st.write(f'Probability: {probability:.4f}')
if __name__ == '__main__':
    main()