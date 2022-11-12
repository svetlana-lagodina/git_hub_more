    # Access each dimension individually
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

    # Or store the dimensions and query them later
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")

    # Set size
driver.set_window_size(1024, 768)

    # Maximize
driver.maximize_window()

    # Minimize
driver.minimize_window()

    # Fullscreen window
driver.fullscreen_window()