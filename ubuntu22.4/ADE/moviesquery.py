from lxml import etree

# Load the XML file with full path
tree = etree.parse('C:/Users/Asus/Desktop/ADE_Lab/ADE_Lab/New folder/movies.xml')
root = tree.getroot()

#lib
# Get all movie titles
print("************************ Movie Titles **************************")
titles = root.xpath('//movie/title/text()')
print("Titles:")
for title in titles:
    print(title)

# Get all movie directors
print("\n\n")
print("************************ All Directors **************************")
directors = root.xpath('//movie/director/text()')
for director in directors:
    print(director)

# Get movies by genre with director
print("\n\n")
print("************************ Movies by Genre with Director **************************")
for movie in root.xpath('//movie'):
    director = movie.xpath('director/text()')[0]
    genre = movie.xpath('genre/text()')[0]
    print(f"Movie: {director} - {genre}")

# Get movies by genre with title
print("\n\n")
print("************************ Movies by Genre with Title **************************")
for genre in set(root.xpath('//movie/genre/text()')):
    movies_in_genre = root.xpath(f"//movie[genre='{genre}']")
    print(f"Movies in {genre}:")
    for movie in movies_in_genre:
        print(f"- {movie.find('title').text}")
