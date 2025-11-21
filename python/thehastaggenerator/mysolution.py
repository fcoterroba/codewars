def generate_hashtag(s):
    if not s: return False
    result = '#' + ''.join(word.capitalize() for word in s.split())
    return result if len(result) <= 140 else False

# original kata: https://www.codewars.com/kata/52449b062fb80683ec000024
# my solution: https://www.codewars.com/kata/reviews/5b86545bb80ee00ca6000358/groups/62f2586e72d18e000122b7ec