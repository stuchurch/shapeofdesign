import streamlit as st
import matplotlib.pyplot as plt
import io
from radar_chart import create_radar_chart # Import the function from the other file

# 1. This must be the very first Streamlit command
st.set_page_config(layout="wide") # Use wide layout for better visual

# 2. Then apply custom CSS for white background and default text color
st.markdown(
    """
   <style>
    .stApp {
        background-color: white;
        color: black; /* Set default text color for the whole app */
    }
    h1, h2, h3, h4, h5, h6 {
        color: black;
    }
    p {
        color: black;
    }
    .stSlider > div > div > div > div { /* Targeting the slider value label */
        color: black !important;
    }

	/* Remove slider labels */ 
    div[data-testid="stSliderTickBarMin"],
    div[data-testid="stSliderTickBarMax"] {
        display: none;
    }


	/* This is the container for the download button */
	div[data-testid="stDownloadButton"] {
		display: flex;
	    justify-content: flex-end; /* Aligns content (the button) to the right */
	}

	/* This is the actual download button */
	div[data-testid="stDownloadButton"] button {
    	background-color: white !important; /* Set background to white */
	    color: black !important;             /* Set text color to black */
    	border: 1px solid black !important;  /* Add a black border for definition */
	    border-radius: 5px !important;       /* Optional: rounds the corners */
	    padding: 0.4em 0.8em !important;       /* Optional: adds some padding */
	}

	/* Style for the button on hover */
	div[data-testid="stDownloadButton"] button:hover {
	    background-color: #f0f0f0 !important; /* A light grey for hover effect */
    	border-color: black !important;
	    color: black !important;


    </style>
    """,
    unsafe_allow_html=True
)

st.title("The Shape of Design")


# Define the dimensions (labels) and their corresponding colors
dimensions = [
    "Business", "Performance", "Tech", "Data & AI", "People & Psychology",
    "Theory of Knowledge", "Systems Thinking", "Ethics & Legal", "Design & Creative"
]

colors = [
    '#437F97', 
    '#3A5867', 
    '#303036', 
    '#5A622D', 
    '#849324', 
    '#C2A31A', 
    '#FFB30F', 
    '#F68D0C', 
    '#EC6608'  
]


# Create two columns for the layout
col1, col2 = st.columns([2, 3]) # Adjust column ratios as needed

with col1:
    #st.header("Skills Assessment") # Add a header for the input section
    user_values = []
    for i, dim in enumerate(dimensions):
        # Create a slider for each dimension
        # The wireframe shows a circle with the color, so we'll simulate this with markdown
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: -15px;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background-color: {colors[i]}; margin-right: 10px;"></div>
                <p style="margin: 0; font-size: 16px; color: black;">{dim}</p>
            </div>
        """, unsafe_allow_html=True)
        # Set initial value to 2
        value = st.slider(f" ", 1, 5, 3, key=dim, label_visibility="collapsed") # Slider from 1-5
        user_values.append(value)

# https://github.com/streamlit/streamlit/issues/5936 - ideas for how to remove axis values 

# Scale the user values (0-5) to 0-100 for the radar chart
scaled_values = [val * 20 for val in user_values] # Scale by 20 (since 5 * 20 = 100)

with col2:
    #st.header("Radar Plot") # Add a header for the plot section
    # Generate the radar chart
    fig = create_radar_chart(scaled_values, dimensions, colors, "")
    st.pyplot(fig) # Display the matplotlib figure in Streamlit
    
    # Create a BytesIO object to save the figure without writing to disk
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=300) # Save the figure as PNG
    buf.seek(0) # Rewind the buffer to the beginning

    # Wrap the download button in an HTML div with a custom class for styling
    st.markdown('<div class="download-button-container">', unsafe_allow_html=True)
    st.download_button(
        label="Download PNG",
        data=buf,
        file_name="shapeofdesign.png",
        mime="image/png")
    st.markdown('</div>', unsafe_allow_html=True) # Close the custom div
