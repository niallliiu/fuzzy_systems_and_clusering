def calculate_total_capacity(speed_kmh, num_lanes, vehicle_data):
    """
    Calculate total road capacity based on vehicle categories and their proportions.

    Parameters:
    - speed_kmh (float): Speed in km/h.
    - num_lanes (int): Number of lanes.
    - vehicle_data (dict): Dictionary with keys as vehicle categories and values as dictionaries
                           containing 'length' (meters), 'safety_time' (seconds), and 'proportion' (decimal).

    Returns:
    - float: Total capacity in vehicles per hour.
    """
    # Convert speed from km/h to m/s
    speed_ms = speed_kmh / 3.6

    # Initialize total capacity
    total_capacity = 0

    # Calculate capacity contribution for each vehicle category
    for category, data in vehicle_data.items():
        # Extract length, safety time, and proportion for the category
        length = data['length']
        safety_time = data['safety_time']
        proportion = data['proportion']

        # Calculate the distance per vehicle (D_i)
        distance = speed_ms * safety_time + length

        # Calculate the time interval per vehicle (T_i)
        time_interval = distance / speed_ms

        # Calculate the capacity for this category (C_i)
        category_capacity = 3600 / time_interval

        # Weighted contribution to the total capacity
        total_capacity += category_capacity * proportion

    # Multiply by the number of lanes
    total_capacity *= num_lanes

    return total_capacity


# Example usage
if __name__ == "__main__":
    # Vehicle categories with lengths, safety times, and proportions
    vehicle_proportions = {
        '<5.6m': {'length': 4.5, 'safety_time': 2, 'proportion': 0.5},
        '5.6m-7.6m': {'length': 6.6, 'safety_time': 2.5, 'proportion': 0.2},
        '7.6m-12.5m': {'length': 10.0, 'safety_time': 3, 'proportion': 0.1},
        '12.5m-16.0m': {'length': 14.0, 'safety_time': 3.5, 'proportion': 0.05},
        '>=16.0m': {'length': 20.0, 'safety_time': 4, 'proportion': 0.1},
        '>=24.0m': {'length': 25.0, 'safety_time': 4.5, 'proportion': 0.05},
    }

    # Calculate total capacity
    speed_kmh = 110  # Speed in km/h
    num_lanes = 2  # Number of lanes
    total_capacity = calculate_total_capacity(speed_kmh, num_lanes, vehicle_proportions)

    print(f"Total Capacity: {total_capacity:.2f} vehicles per hour")
