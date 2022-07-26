from PIL import Image, ImageDraw, ImageFont

c = 0
inc = 20
background_img='mossholder'
def create_image_with_text(column, text):
    global c, inc
    background = "app/podcast/"+(background_img)+".jpg"
    img = Image.open(background)
    w,h = img.size
    draw = ImageDraw.Draw(img)
    # print('Column', (h // 10) + (column * 55))
    draw.text((w // 25, (h // 10) + (column * 55)), text, font = fnt, fill=(c,c,c))
    c += inc 
    return img 
     
# def create_image_with_text(size, text):
#     img = Image.new('RGB', (600, 50), "yellow")
#     draw = ImageDraw.Draw(img)
#     draw.text((size[0], size[1]), text, font = fnt, fill="black")
#     return img
 
frames = [] 
 
def roll(text, index):
    # column += 1  
    column = index % 4 
    for i in range(len(text)+1):
        new_frame = create_image_with_text(column, text[:i])
        frames.append(new_frame)

# <<< ========== Customize font and text below ============== >>>>

font_path = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"
fnt = ImageFont.truetype(font_path,28)
 
def generate_animator(id,tweet, background):
    line = 44
    global background_img 
    background_img = background
    # tweet = tweet.splitlines()
    # [roll(text) for text in tweet]
    thread = [(tweet[text:text+line]) for text in range(0, len(tweet), line)]

    for i in range(len(thread)):
        roll(thread[i], i)
    # <<< ======================================================== >>>
    filename = './app/assets/media/'+ str(id)+'.gif'
    frames[0].save(filename, format='GIF', 
        append_images=frames[1:], save_all=True, duration=80, loop=0)
    
    return filename

 
# tweet = """5 Things Every Woman Should Do Immediately After Having Intercourse To Keep The Vagina Healthy

# A thread
# 1. Use the bathroom before and after intercourse

# You can reduce your risk of contracting urinary tract infections and regulate your lady's part pH level by using the bathroom after having intercourse.
# 2. Make sure you wipe from front to back

# The right way to wipe after having intercourse to prevent the building up of harmful bacteria that may probably cause UTIs is frm front to bck.This is because if U are wiping from the back to the front, U may contaminate the lady's part
# 3. Always let yourself dry off after you take a shower

# It is important to note that excess moisture and warmth are a breeding ground for infections, so make sure your female organ is not left moist before you put on your panties.
# 4. Gently clean the area

# All you will need for the cleaning up should be mild soap and water. You can gently wash out sweat, semen, and bacteria by wiping from front to back using mild soap and water.
# 5. Avoid douching with all possible efforts
# Douching is a very bad habit and should be avoided by every lady. One of the bad effects of douching is that it removes the healthy bacteria in your female organ thereby making it prone to infections and diseases."""

# generate_animator(tweet, '')