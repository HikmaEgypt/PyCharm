/**
 * Created by akelsaman on 12/18/15.
 */
//"^((?!  )[ a-zA-Z\u0621-\u063A\u0641-\u064A]){3,50}$"
var onPageLoad = true;
var validatorEvents = "change input keyup paste propertychange";
//var validatorEvents = "change";
var validatorPatterns = {
    /*refuse*/
    "Empty":"^$",
    "Spcs":"[ ][ ]",
    "Dts":"[.][.]",
    "Dshs":"[-][-]",
    "Min03":"^.{1,2}$",
    "Max50":"^.{51,}$",
    /*accept*/
    "Dg":"^[0-9]+$",
    "EgyptianMobile":"^01[0-2][0-9]{8}$",
    "Email":"^[a-zA-Z0-9][_a-zA-Z0-9]+[@][a-zA-Z0-9][-.a-zA-Z0-9]+[a-zA-Z0-9][.][a-zA-Z]{2,10}$",
    "Ar":"^[\u0621-\u063A\u0641-\u064A]+$",
    "EnSmCp":"^[a-zA-Z]+$",
    "EnSmCpArSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]+$",
    "EnSmCpArDgSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]+$"
    //"EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]{3,50}$"
};
var validatorMessages = {
    /*refuse*/
    "Empty":"Required can not be empty",
    "Spcs":"Can not use more than one space in series",
    "Dts":"Can not use more than one dot (.) in series",
    "Dshs":"Can not use more than one dash (-) in series",
    "Min03":"Can not be less than 03 character",
    "Max50":"Can not be more than 50 character",
    /*accept*/
    "Dg":"Digits only",
    "EgyptianMobile":"Enter valid mobile number, Example: 01012345678",
    "Email":"Enter valid Email, Example: someone@example.com",
    "Ar":"Accepts only Arabic characters",
    "EnSmCp":"Accepts only Small&Capitals English",
    "EnSmCpArSpc":"Accepts small&Capital English and Arabic characters",
    "EnSmCpArDgSpc":"Accepts small&Capital English, Arabic and Digits characters"
    //"EnSmCpArDgSpc0350":"Accepts 3-50 small&Capital English, Arabic and Digits characters"
};