import brewcalculators
import sys

def main():
    # WaterVolInQuarts, GrainMassInPounds, GrainTemp, MashTemp
    print brewcalculators.calc_strike_temp(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    pass


if __name__ == '__main__':
    main()
