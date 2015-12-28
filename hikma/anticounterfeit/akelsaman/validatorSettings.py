validatorPatterns = {
    #refuse
    "Empty":"^$",
    "Spcs":"[ ][ ]",
    "Dts":"[.][.]",
    "Dshs":"[-][-]",
    "Min03":"^.{1,2}$",
    "Max50":"^.{51,}$",
    #accept
    "EgyptianMobile":"^01[0-2][0-9]{8}$",
    "Email":"^[a-zA-Z0-9][_a-zA-Z0-9]+[@][a-zA-Z0-9][-.a-zA-Z0-9]+[a-zA-Z0-9][.][a-zA-Z]{2,10}$",
    "Dg":"^[0-9]+$",
    "Ar":"^[\u0621-\u063A\u0641-\u064A]+$",
    "ArDgSpc":"^[ 0-9\u0621-\u063A\u0641-\u064A]+$",
    "EnSmCp":"^[a-zA-Z]+$",
	"EnSmCpDg":"^[a-zA-Z0-9]+$",
    "EnSmCpArSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]+$",
    "EnSmCpArDgSpc":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]+$"
    #"EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]{3,50}$"
}
validatorMessages = {
    #refuse
    "Empty":"Required can not be empty",
    "Spcs":"Can not use more than one space in series",
    "Dts":"Can not use more than one dot (.) in series",
    "Dshs":"Can not use more than one dash (-) in series",
    "Min03":"Can not be less than 03 character",
    "Max50":"Can not be more than 50 character",
    #accept
    "EgyptianMobile":"Enter valid mobile number, Example: 01012345678",
    "Email":"Enter valid Email, Example: someone@example.com",
    "Dg":"Digits only",
    "Ar":"Accepts only Arabic characters",
    "ArDgSpc":"Arabic characters, Digits and Space only",
    "EnSmCp":"Accepts only Small&Capitals English",
	"EnSmCpDg":"Accepts only Small&Capitals English and Digits",
    "EnSmCpArSpc":"Accepts small&Capital English and Arabic characters",
    "EnSmCpArDgSpc":"Accepts small&Capital English, Arabic and Digits characters"
    #"EnSmCpArDgSpc0350":"Accepts 3-50 small&Capital English, Arabic and Digits characters"
}