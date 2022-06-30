import Cookies from 'js-cookie'

var param = {path: '/', domain: document.domain.match(/[^\.]+\.[^\.]+$/)[0]}
export function getToken() {
  var tokenName = Cookies.get('token_name', param)
  if(tokenName){
    return Cookies.get(tokenName,param)
  }else{
    return false
  }
}
