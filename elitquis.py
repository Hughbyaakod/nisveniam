if l_ms is not None:
    minutes, seconds = divmod(l_ms // 1000, 60)
    print(f"Duration: {minutes} minutes and {seconds} seconds")
else:
    print("Duration key not found in metadata.")
