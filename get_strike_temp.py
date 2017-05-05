import brewcalculators
import sys, json

def main():
    # WaterVolInQuarts, GrainMassInPounds, GrainTemp, MashTemp
    json.dump(brewcalculators.calc_strike_temp(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])), sys.stdout)
    pass


if __name__ == '__main__':
    main()
