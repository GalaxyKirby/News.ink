import splat3_api

def run_tests():
    test_api_calls()

def test_api_calls():
    data = splat3_api.fetch_schedule_data()

    current_rotos = []

    future_rotos = []

    # Current Rotations 
    try:
        turf_war_roto = splat3_api.parse_scedule_data(data, 0, splat3_api.MatchType.REGULAR)

        current_rotos.append(turf_war_roto)

    except Exception as e:
        print(f"CURRENT TURF ROTO FAILED: {str(e)}")

    try:
        open_roto = splat3_api.parse_scedule_data(data, 0, splat3_api.MatchType.OPEN)

        current_rotos.append(open_roto)

    except Exception as e:
        print(f"CURRENT OPEN ROTO FAILED: {str(e)}")

    try:
        series_roto = splat3_api.parse_scedule_data(data, 0, splat3_api.MatchType.SERIES)

        current_rotos.append(series_roto)

    except Exception as e:
        print(f"CURRENT SERIES ROTO FAILED: {str(e)}")

    try:
        x_roto = splat3_api.parse_scedule_data(data, 0, splat3_api.MatchType.X_BATTLE)

        current_rotos.append(x_roto)

    except:
        (f"CURRENT X ROTO FAILED: {str(e)}")

    for r in current_rotos:
        print(f"Current {r.name}")
        print(f"{r.mode} | {r.map1.name} | {r.map2.name}")
        print("===============")

    # Future Rotations
    try:
        turf_war_roto_f = splat3_api.parse_scedule_data(data, 1, splat3_api.MatchType.REGULAR)     

        future_rotos.append(turf_war_roto_f)

    except Exception as e:
        print(f"CURRENT TURF ROTO FAILED: {str(e)}")

    try:
        open_roto_f = splat3_api.parse_scedule_data(data, 1, splat3_api.MatchType.OPEN)

        future_rotos.append(open_roto_f)

    except Exception as e:
        print(f"CURRENT OPEN ROTO FAILED: {str(e)}")

    try:
        series_roto_f = splat3_api.parse_scedule_data(data, 1, splat3_api.MatchType.SERIES)

        future_rotos.append(series_roto_f)

    except Exception as e:
        print(f"CURRENT SERIES ROTO FAILED: {str(e)}")

    try:
        x_roto_f = splat3_api.parse_scedule_data(data, 1, splat3_api.MatchType.X_BATTLE)

        future_rotos.append(x_roto_f)

    except Exception as e:
        (f"CURRENT X ROTO FAILED: {str(e)}")

    for r in future_rotos:
        print(f"Next {r.name}")
        print(f"{r.mode} | {r.map1.name} | {r.map2.name}")
        print("===============")

# Run whatever tests are put into this function
run_tests()