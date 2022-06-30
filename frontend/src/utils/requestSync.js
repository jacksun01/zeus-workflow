import $ from 'jquery'

const requestSync = {
  deal(url, data, method,timeout=2000) {
    var ret = null
    try {
      $.ajax({
        url: url,
        type: method,
        async: false,
        data: data,
        timeout: timeout,
        beforeSend: function (xhr) {
        },
        success: function (data, textStatus, jqXHR) {
          ret = data
        },
        error: function (xhr, textStatus) {
          ret = null
        },
        complete: function () {
        }
      })
    } catch (err) {
      console.log(err)
    }
    return ret
  },
}
export {requestSync}
