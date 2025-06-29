import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(data, labels, colors, chart_title=""):
    """
    Creates a beautiful radar chart with specified dimensions and colors.

    Args:
        data (list): A list of numerical values for each dimension.
                     Values should be between 0 and 100 for proper scaling.
        labels (list): A list of strings, representing the names of each dimension.
        colors (list): A list of hex color codes for each dimension.
        chart_title (str, optional): The title of the radar chart. Defaults to "Radar Chart".
    """

    num_dimensions = len(labels)

    # Calculate angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_dimensions, endpoint=False).tolist()

    # The data must be 'circular', so we append the first value to the end
    data = data + data[:1]
    angles = angles + angles[:1]

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Set up the background for the chart
    ax.set_facecolor('#efefef') # Light grey background for the plot area
    fig.patch.set_facecolor('#FFFFFF') # White background for the figure

    # Remove spines
    ax.spines["start"].set_color("none")
    ax.spines["polar"].set_color("none")

    # Draw the radar chart for each dimension
    for i in range(num_dimensions):
        # Create a single segment for each dimension
        # Data points for the segment (0, value, value, 0)
        segment_angles = [angles[i], angles[i], angles[i+1], angles[i+1], angles[i]]
        segment_data = [0, data[i], data[i], 0, 0] # Start from center, go to value, then back to center

        # Fill the segment with the corresponding color
        ax.fill(segment_angles, segment_data, color=colors[i], alpha=1,
                label=labels[i] if i < num_dimensions else "") # Only label once per segment

    # Set the y-axis (radial axis) limits and ticks
    ax.set_ylim(0, 100) # Values are scaled to 0-100 before passing to this function
    ax.set_yticks([])
    ax.set_yticklabels([])

    # Calculate the midpoint angles for the labels
    # Each label should be centered between the two adjacent axes
    label_angles = [a + (np.pi / num_dimensions) for a in angles[:-1]]
    ax.set_xticks(label_angles) # Set the new tick positions for labels
    ax.set_xticklabels(labels, size=12, color="black") # Changed color to black
    
    ax.xaxis.grid(False) # Turn off radial grid lines
    ax.yaxis.grid(True, linestyle='--', alpha=0.7, color='lightgray')

    # Add a title
    ax.set_title(chart_title, size=16, color="black", y=1.1) # Changed color to black

    # Adjust layout to prevent labels from overlapping
    plt.tight_layout()

    return fig # Return the figure object instead of showing it