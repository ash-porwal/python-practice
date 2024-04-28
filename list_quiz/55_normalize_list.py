def flatten_list(nested_list):
    flat_list = []
    
    def flatten(items):
        for item in items:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_list.append(item)
    
    flatten(nested_list)
    return flat_list

# Example nested list
nested_list = [
    [
        [
            [1, 2], [3, 4]
        ],
        [
            [5, 6], [7, 8]
        ]
    ],
    [
        [
            [9, 10], [11, 12]
        ],
        [
            [13, 14], [15, 16]
        ],
        [
            100,200
        ]
    ]
]

# Normalize the nested list
normalized_list = flatten_list(nested_list)
print(normalized_list)

