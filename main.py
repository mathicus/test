import streamlit as st
import numpy as np

def generate_random_vectors(n):
  """Generates a list of n random vectors."""
  vectors = []
  for _ in range(n):
    vector = np.random.randint(-100, 100, size=2)
    vectors.append(vector)
  return vectors

def main():
  """Creates the Streamlit app."""
  n = st.number_input("Number of vectors:", 10, 100, 10)
  vectors = generate_random_vectors(n)
  st.title("Cartesian Graph with Random Vectors")
  st.plot(vectors)

if __name__ == "__main__":
  main()
