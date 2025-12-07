
resturants =[
    {"id":1, "name":"KFC"},
    {"id":2, "name":"McDonalds"}
    ]

ratings=[{"resturant_id":1, "rating":4},
         {"resturant_id":1, "rating":5},
         {"resturant_id":2, "rating":3}
        ]

def solve(resturants, ratings):
    rating_map={}

    for r in ratings:
        rid= r["resturant_id"]
        
        rating_map.setdefault(rid,[]).append(r["rating"])
    print(rating_map)
    result =[]
    for res in resturants:
        rid=res["id"]
        scores=rating_map.get(rid,[])
        avg = sum(scores)/len(scores)
        result.append({
            "id":rid,
            "name":res["name"],
            "average_rating":avg
        })

    result.sort(key=lambda x: x["average_rating"],reverse=True)
    return result

print(solve(resturants, ratings))