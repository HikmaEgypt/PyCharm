validatorPatterns = {
	# refuse
	"Empty": "^$",
	"Spcs": "[ ][ ]",
	"Dts": "[.][.]",
	"Dshs": "[-][-]",
	"Month01-12": "^2015.([1][3-9]|[2-9][0-9])",
	"Min03": "^.{1,2}$",
	"Max50": "^.{51,}$",
	# accept
	"internalOrExternal": "^Internal$|^External$",
	"EgyptianMobile": "^01[0-2][0-9]{8}$",
	"Email": "^[a-zA-Z0-9][_a-zA-Z0-9]+[@][a-zA-Z0-9][-.a-zA-Z0-9]+[a-zA-Z0-9][.][a-zA-Z]{2,10}$",
	"YYYY.MM.DD HH:MM": "^2015.([0][1-9]|[1][0-2]).([0-2][0-9]|[3][0-1]) ([0-1][0-9]|[2][0-3]):[0-5][0-9]$",
	"Dg": "^[0-9]+$",
	"Ar": "^[\u0621-\u063A\u0641-\u064A]+$",
	"ArDgSpc": "^[ 0-9\u0621-\u063A\u0641-\u064A]+$",
	"EnSmCp": "^[a-zA-Z]+$",
	"EnSmCpDg": "^[a-zA-Z0-9]+$",
	"EnSmCpArSpc": "^[ a-zA-Z\u0621-\u063A\u0641-\u064A]+$",
	"EnSmCpArDgSpc": "^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]+$"
	# "EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A0-9]{3,50}$"
}
validatorMessages = {
	# refuse
	"Empty": "Required can not be empty",
	"Spcs": "Can not use more than one space in series",
	"Dts": "Can not use more than one dot (.) in series",
	"Dshs": "Can not use more than one dash (-) in series",
	"Month01-12": "Month accepts only from 01 to 12",
	"Min03": "Can not be less than 03 character",
	"Max50": "Can not be more than 50 character",
	# accept
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
	"EnSmCpArDgSpc": "Accepts small&Capital English, Arabic and Digits characters"
	# "EnSmCpArDgSpc0350":"Accepts 3-50 small&Capital English, Arabic and Digits characters"
}
