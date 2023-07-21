const request = require('request');

var client_id = 'a744e34892764607a6c064f4729b1e20';
var client_secret = '5184322668bf40e89fe584fd60feb768';

var authOptions = {
  url: 'https://accounts.spotify.com/api/token',
  headers: {
    Authorization:
      'Basic ' +
      new Buffer.from(client_id + ':' + client_secret).toString('base64'),
  },
  form: {
    grant_type: 'client_credentials',
  },
  json: true,
};

request.post(authOptions, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    var token = body.access_token;
    console.log(body);
  }
});
