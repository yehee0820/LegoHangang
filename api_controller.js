"use strict";
exports.__esModule = true;
var graphql_request_1 = require("graphql-request");
var endpoint = "https://pcmap-api.place.naver.com/graphql";
var query = "{\n            data {\n                restaurants {\n                       items {\n                          name\n                          microReview\n                          priceCategory\n                          roadAddress\n                          visitorReviewScore\n                          blogCafeReviewCount\n                          businessCategory\n                          businessHours\n                          category\n                        }\n                      }\n                      }\n                    }";
graphql_request_1.request(endpoint, query).then(function (data) {
    return console.log(JSON.stringify(data, null, 2));
});
