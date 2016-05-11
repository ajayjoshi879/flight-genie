# Flight Genie

Trying to predict flight prices with NN

## Installation

```
sh
# you have to have python 3 installed
pyenv env
source env/bin/activate
pip install -r requirements.txt
python flight_genie/main.py
```

Then every time before working activate virtual env
```
sh
source env/bin/activate
invoke run -e <training_csv_file.csv> -t <testing_csv_file.csv>
```


## Features wanted:

 - in-code ability to infer and filter data columns
 - plots
 - success rate


## User input

Indented things can be inferred.

 - date
  - dayofmonth
  - weekday
 - outbounddate
  - outbounddayofmonth
  - outboundweekday
 - inbounddate
  - inbounddayofmonth
  - inboundweekday
 - originairport
  - origincitycode
  - origincountry
 - destinationairport
  - destinationcitycode
  - destinationcountry
 - carriercode
 - carriertype
 - adults
 - children
  - daystodeparture
  - dayslengthofstay
 - priceusd
 - platform
 - isota
 - pk_exitid
 - origdestcitycode


# Help

```
invoke -h
```
