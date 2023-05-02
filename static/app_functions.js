function getUrlParams(urlOrQueryString) {
    if ((i = urlOrQueryString.indexOf('?')) >= 0) {
        const queryString = urlOrQueryString.substring(i + 1);
        if (queryString) {
            return _mapUrlParams(queryString);
        }
    }

    return {};
}

/**
 * Helper function for `getUrlParams()`
 * Builds the querystring parameter to value object map.
 *
 * @param queryString {string} - The full querystring, without the leading '?'.
 */
function _mapUrlParams(queryString) {
    return queryString
        .split('&')
        .map(function (keyValueString) {
            return keyValueString.split('=')
        })
        .reduce(function (urlParams, [key, value]) {
            if (Number.isInteger(parseInt(value)) && parseInt(value) == value) {
                urlParams[key] = decodeURIComponent(parseInt(value));
            } else {
                urlParams[key] = decodeURIComponent(value);
            }
            return urlParams;
        }, {});
}


function getDateTime(d) {
    /* Gets the date time with a day offset of d */
    /* This will always use the current date and then apply the offset */
    var date = new Date();
    console.log("date = " + date)
    date.setDate(date.getDate() + d)
    let hour = date.getHours();
    let min = date.getMinutes();
    let sec = date.getSeconds();
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    hour = (hour < 10 ? "0" : "") + hour;
    min = (min < 10 ? "0" : "") + min;
    sec = (sec < 10 ? "0" : "") + sec;
    month = (month < 10 ? "0" : "") + month;
    day = (day < 10 ? "0" : "") + day;
    // return year + "-" + month + "-" + day + "T" + hour + ":" + min + ":" + sec;

    return year + "-" + month + "-" + day;

}

function getDateTimeQS(d)
{
    /* Gets the date time span from the query string then applies the day offset */
}
