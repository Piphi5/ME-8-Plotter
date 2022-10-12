import matplotlib.pyplot as plt
import streamlit  as st

st.title("ME8 Graph Generator")

t = st.text_area("Enter test output")
columns = [x.strip() for x in st.text_input("Enter columns separated by , (have timestamp as the first variable)", value="timestamp, pan, tilt").split(",")]


if t and len(columns) > 0:
    data_dict = {col : list() for col in columns}
    for line in t.split("\n"):
        data_group = zip(columns,line.split(" "))
        for group in data_group:
            col, val = group
            data_dict[col].append(float(val))

    for values in [col for col in columns[1:]]:
        plt.figure()
        plt.plot(data_dict[columns[0]], data_dict[values])
        plt.title(f"{values} vs time")

    for num in plt.get_fignums():
        fig = plt.figure(num)
        st.pyplot(fig)