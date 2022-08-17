import streamlit as st
import pickle


filename = "model.sv"
model = pickle.load(open(filename,'rb'))

price_ranges = {
    0: "low cost" ,
    1: "medium cost",
    2: "high cost",
    3: "very high cost"
}

def main():
    st.set_page_config(page_title="Mobile price prediciton")
   
    three_g = 1 if st.checkbox("Has 3G?") else 0
    four_g = 1 if st.checkbox("Has 4G?") else 0
    touch_screen = 1 if st.checkbox("Has Touch screen?") else 0
    wifi = 1 if st.checkbox("Has WiFi?") else 0
    blue = 1 if st.checkbox("Has Bluetooth?") else 0
    dual_sim = 1 if st.checkbox("Has dual sim?") else 0
    battery_power = st.number_input("Battery power", min_value = 0)
    clock_speed = st.number_input("Clock speed", min_value = 0.0)
    fc = st.number_input("Front Camera mega pixels", min_value = 0)
    int_memory = st.number_input("Internal memory in GB", min_value = 0)
    n_cores = st.number_input("Number of cores of processor", min_value = 0)
    pc = st.number_input("Primary Camera mega pixels", min_value = 0)
    ram = st.number_input("RAM in MB", min_value = 0)
    talk_time = st.number_input("Longest time that a single battery charge will last when you are talking on the phone", min_value = 0)
    
    data = [[battery_power, blue, clock_speed, dual_sim, fc, four_g,
       int_memory, n_cores, pc,ram, talk_time, three_g,
       touch_screen, wifi]]
    price_range = model.predict(data)
    
    st.header(f"Price range: {price_ranges[price_range[0]]}")
    
    
if __name__ == "__main__":
    main()