import json

def ParseMetar(data):
    SplitMetar = data.split("\n")
    SplitDate = SplitMetar[0].split(" ")
    Date = SplitDate[0]
    Time = SplitDate[1]

    ReadingData = SplitMetar[1].split(" ")

    StationName = ReadingData[0]

    RawWindData = ReadingData[3]
    WindDir = int(RawWindData[:3])
    WindSpeed = int(RawWindData[3:len(RawWindData)-2])

    RawVisibility = ReadingData[4]
    Visibility = int(RawVisibility[:len(RawVisibility)-2])

    RawObservation = ReadingData[5]
    IsClear = False
    if(RawObservation == "CLR"):
        IsClear = True

    RawTempDew = ReadingData[6].split("/")
    Temp = int(RawTempDew[0])
    DewPoint = int(RawTempDew[1])

    e = 2.71828
    Humidity = round(100 * abs((e**((17.625*DewPoint)/(243.04+DewPoint)))/(e**((17.625*Temp)/(243.04+Temp)))), 2)

    RawPressure = ReadingData[7]
    Pressure = float(f"{RawPressure[1:3]}.{RawPressure[3:5]}")

    WeatherData = {
        "StationName":StationName,
        "WindDir":WindDir,
        "WindSpeed":WindSpeed,
        "Visibility":Visibility,
        "Clear":IsClear,
        "Temperature":Temp,
        "DewPoint":DewPoint,
        "Humidity":Humidity,
        "Pressure":Pressure
    }

    return WeatherData