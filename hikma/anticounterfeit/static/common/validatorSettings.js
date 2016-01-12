/**
 * Created by akelsaman on 12/18/15.
 */
//"^((?!  )[ a-zA-Z\u0621-\u063A\u0641-\u064A]){3,50}$"
var onPageLoad = false;
// var validatorEvents = "change input keyup paste propertychange";
var validatorEvents = "change";
var validatorPatterns = {
	// refuse
	"Empty": "^$",
	"Spcs": "[ ][ ]",
	"Dts": "[.][.]",
	"Dshs": "[-][-]",
	"Month01-12": "^.*[.]([1][3-9]|[2-9][0-9])[.]",
	"MonthFormatIsWrong": "^.*[.]([0-9]{0,1}|[0-9]{3,})[.]",
	"Day01-31": "^.*[.].*[.]([3][2-9]|[4-9][0-9]) ",
	"DayFormatIsWrong": "^.*[.].*[.]([0-9]{0,1}|[0-9]{3,})[ ]",
	"Hour00-23": "^.*[.].*[.].* ([2][4-9]|[3-9][0-9])[:]",
	"HourFormatIsWrong": "^.*[.].*[.].* ([0-9]{0,1}|[0-9]{3,})[:]",
	"Minute00-59": "^.*[.].*[.].* .*:([6-9][0-9])$",
	"MinuteFormatIsWrong": "^.*[.].*[.].* .*:([0-9]{0,1}|[0-9]{3,})$",
	"Min03": "^.{1,2}$",
	"Max50": "^.{51,}$",
	// accept
	"internalOrExternal": "^Internal$|^External$",
	"EgyptianMobile": "^01[0-2][0-9]{8}$",
	"Email": "^[a-zA-Z0-9][_a-zA-Z0-9]+[@][a-zA-Z0-9][-.a-zA-Z0-9]+[a-zA-Z0-9][.][a-zA-Z]{2,10}$",
	"YYYY.MM.DD HH:MM": "^2016[.]([0][1-9]|[1][0-2])[.]([0-2][0-9]|[3][0-1]) ([0-1][0-9]|[2][0-3])[:][0-5][0-9]$",
	"Dg": "^[0-9]+$",
	"Ar": "^[\u0621-\u063A\u0641-\u064A]+$",
	"ArDgSpc": "^[ 0-9\u0621-\u063A\u0641-\u064A]+$",
	"EnSmCp": "^[a-zA-Z]+$",
	"EnSmCpDg": "^[a-zA-Z0-9]+$",
	"EnSmCpArSpc": "^[ a-zA-Z\u0621-\u063A\u0641-\u064A]+$",
	"EnSmCpArDgSpc": "^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]+$",
	"Any": "^.+$",
	// "EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]{3,50}$",
};
var validatorMessages = {
	// refuse
	"Empty": "Required can not be empty",
	"Spcs": "Can not use more than one space in series",
	"Dts": "Can not use more than one dot (.) in series",
	"Dshs": "Can not use more than one dash (-) in series",
	"Month01-12": "Month accepts only from 01 to 12",
	"MonthFormatIsWrong": "Kindly enter valid month in correct format of 2 digits ex: 09",
	"Day01-31": "Day accepts only from 01 to 31",
	"DayFormatIsWrong": "Kindly enter valid day in correct format of 2 digits ex: 05",
	"Hour00-23": "Hour accepts only from 00 to 23",
	"HourFormatIsWrong": "Kindly enter valid Hour in correct format of 2 digits ex: 08",
	"Minute00-59": "Minute accepts only from 00 to 59",
	"MinuteFormatIsWrong": "Kindly enter valid Minute in correct format of 2 digits ex: 06",
	"Min03": "Can not be less than 03 character",
	"Max50": "Can not be more than 50 character",
	// accept
	"internalOrExternal": "Accepts only Internal or External word",
	"EgyptianMobile": "Enter valid mobile number, Example: 01012345678",
	"Email": "Enter valid Email, Example: someone@example.com",
	"YYYY.MM.DD HH:MM":"Kindly enter valid date and time in the correct format 2015.12.29 16:44",
	"Dg": "Digits only",
	"Ar": "Accepts only Arabic characters",
	"ArDgSpc": "Arabic characters, Digits and Space only",
	"EnSmCp": "Accepts only Small&Capitals English",
	"EnSmCpDg": "Accepts only Small&Capitals English and Digits",
	"EnSmCpArSpc": "Accepts small&Capital English and Arabic characters",
	"EnSmCpArDgSpc": "Accepts small&Capital English, Arabic and Digits characters",
	"Any": "Accepts any character",
	//"EnSmCpArDgSpc0350":"Accepts 3-50 small&Capital English, Arabic and Digits characters",
};