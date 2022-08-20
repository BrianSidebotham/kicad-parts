# TE Val-U-Lok Connector Series KiCAD Library

This library contains vertical connectors for KiCAD from the TE Val-U-Lok series.

Several series in these connectors are basically identical except for the material used for the plastic.

- [VAL-U-LOK Connector System](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=1773458-6_VAL-U-LOK_QRG&DocType=DS&DocLang=EN)
- [High Current VAL-U-LOK](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7F1-1773979-5_13A_VAL-U-LOK_Connectors%7FA619%7Fpdf%7FEnglish%7FENG_DS_1-1773979-5_13A_VAL-U-LOK_Connectors_A619.pdf)

## Getting Started

You can simply clone this repository somewhere are reference it in your global library table.

To develop the parts, create a python virtual environment and update the packages that should already be available:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install --upgrade setuptools wheel pip
```

Install the requirements for this library:

```shell
$ python -m pip install -r requirements.txt
```
