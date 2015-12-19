/**
 * Created by akelsaman on 12/18/15.
 */
//"^((?!  )[ a-zA-Z\u0621-\u063A\u0641-\u064A]){3,50}$"
var onPageLoad = false;
//var validatorEvents = "change input keyup paste propertychange";
var validatorEvents = "change";
var validatorPatterns = {
    "Empty":"^$",
    "Min03":"^.{1,2}$",
    "Max50":"^.{51,}$",
    "Spcs":"[ ][ ]",
    "Dts":"[.][.]",
    "Dshs":"[-][-]",
    "Dg":"^[0-9]+$",
    "EgyptianMobile":"^01[0-2][0-9]{8}$",
    "Email":"^[_a-zA-Z0-9]+@[.-a-zA-Z0-9]+.[a-zA-Z]{2,10}$",
    "EnSmCpArSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]+$",
    "EnSmCpArDgSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]+$"
    //"EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]{3,50}$"
};
var validatorMessages = {
    "Empty":"Required Can not be empty",
    "Min03":"Can not be less than 03 character",
    "Max50":"Can not be more than 50 character",
    "Spcs":"Can not use more than one space in series",
    "Dts":"Can not use more than one dot (.) in series",
    "Dshs":"Can not use more than one dash (-) in series",
    "Dg":"Digits only",
    "EgyptianMobile":"Enter valid mobile number, Example: 01012345678",
    "Email":"Enter valid Email, Example: someone@example.com",
    "EnSmCpArSpc":"Accepts small&Capital English and Arabic characters",
    "EnSmCpArDgSpc":"Accepts small&Capital English, Arabic and Digits characters"
    //"EnSmCpArDgSpc0350":"Accepts 3-50 small&Capital English, Arabic and Digits characters"
};