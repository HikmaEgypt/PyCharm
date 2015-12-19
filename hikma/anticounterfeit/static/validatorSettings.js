/**
 * Created by akelsaman on 12/18/15.
 */
//"^((?!  )[ a-zA-Z\u0621-\u063A\u0641-\u064A]){3,50}$"
var onPageLoad = true;
var validatorEvents = "change input keyup paste propertychange";
//var validatorEvents = "change";
var validatorPatterns = {
    "Empty":"^$",
    "Min03":"^.{1,2}$",
    "Max50":"^.{51,}$",
    "Spcs":"[ ][ ]",
    "Dg":"^[0-9]+$",
    "EnSmCpArSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]+$",
    "EnSmCpArDgSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]+$"
    //"EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]{3,50}$"
};
var validatorMessages = {
    "Empty":"Required Can not be empty",
    "Min03":"Can not be less than 03 character",
    "Max50":"Can not be more than 50 character",
    "Spcs":"Can not use more than one space",
    "Dg":"Digits only",
    "EnSmCpArSpc":"Accepts small&Capital English and Arabic characters",
    "EnSmCpArDgSpc":"Accepts small&Capital English, Arabic and Digits characters"
    //"EnSmCpArDgSpc0350":"Accepts 3-50 small&Capital English, Arabic and Digits characters"
};