 import { request } from "graphql-request"

        const endpoint = "https://pcmap-api.place.naver.com/graphql"
        const query = `{
            data {
                restaurants {
                       items {
                          name
                          microReview
                          priceCategory
                          roadAddress
                          visitorReviewScore
                          blogCafeReviewCount
                          businessCategory
                          businessHours
                          category
                        }
                      }
                      }
                    }`

        request(endpoint, query).then((data) =>
            console.log(JSON.stringify(data, null, 2))
        )

 declare var libraryVar: any;