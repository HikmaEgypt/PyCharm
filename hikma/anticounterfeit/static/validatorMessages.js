/**
 * Created by akelsaman on 12/18/15.
 */
//"^((?!  )[ a-zA-Z\u0621-\u063A\u0641-\u064A]){3,50}$"
//var validatorMessages = {"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]{3,50}$":"Error"};
/*var validatorRules = '{"rule":[' +
'{"EnSmCpArDgSpc0350":"", "regularExpresionPattern":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]{3,50}$", "Message":"Error"}' +
']}';*/
var validatorPatterns = {
    "DblSpc":"[ ][ ]",
    "EnSmCpArDgSpc0350":"^[ a-zA-Z\u0621-\u063A\u0641-\u064A]{3,50}$"
};
var validatorMessages = {
    "DblSpc":"Can not use double space",
    "EnSmCpArDgSpc0350":"Error"
};