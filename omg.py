import math

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

class Booklet:
    """Booklet representation"""
    images_count = 0
    documents_per_page = 0 #dozwolone 1 albo 2
    booklet_pages_count = 0 #obliczne w konstruktorze
    images_in_booklet = []
    currently_returnet_image = 0
    booklet_sheets_count = 0

    def __init__(self, images_count, documents_per_page):
        self.documents_per_page = documents_per_page
        self.booklet_pages_count = math.ceil(images_count / 4) * 4 ## Założenie, że zawsze parzyste
        self.booklet_sheets_count = math.ceil(images_count / 4)

    def assign_images(self, images):
        self.images_in_booklet = []
        self.currently_returnet_image = 0
        current_sheet = 1
        if self.booklet_sheets_count == 1:
            i = 1
            current_page = 1
            for image in images:
                horizontal_snap = i % 2
                self.images_in_booklet.append(BookletImage(image, horizontal_snap, 0, current_page, current_sheet, "A"))
                i = i + 1
                if i % 2 == 0:
                    current_page = current_page + 1
                if i % 4 == 0:
                    current_page = current_page - 2
        elif self.booklet_sheets_count > 1:
            i = 1
            current_page = 1
            direction = 1
            RIGHT = 1
            LEFT = 0
            edge = -1
            for n in range(0, int(self.booklet_pages_count/2)):
                if n >= len(images): 
                    break
                image = images[n]
                if i % 2 == 0:
                    edge = LEFT
                else:
                    edge = RIGHT
                self.images_in_booklet.append(BookletImage(image, edge, 0, current_page, current_sheet, "A"))
                i = i + 1
                if n == int(self.booklet_pages_count/2) - 1:
                    break
                else:
                    current_page = current_page + 1
                if i % 2 == 1:
                    current_sheet = current_sheet + 1

            for n in range(int(self.booklet_pages_count/2), self.booklet_pages_count):
                if n >= len(images): 
                    break
                image = images[n]
                if i % 2 == 0:
                    edge = LEFT
                else:
                    edge = RIGHT
                self.images_in_booklet.append(BookletImage(image, edge, 0, current_page, current_sheet, "A"))
                if n == self.booklet_pages_count:
                    break
                i = i + 1
                current_page = current_page - 1
                if i % 2 == 1:
                    current_sheet = current_sheet - 1

            
                # if current_sheet != self.booklet_sheets_count:
                #     imageA = images[n]
                #     self.images_in_booklet.append(BookletImage(imageA, right, 0, current_page, current_sheet, "A"))
                #     if n + 1 >= len(images):
                #         break
                #     imageB = images[n + 1]
                #     current_page = current_page + 1
                #     self.images_in_booklet.append(BookletImage(imageB, left, 0, current_page, current_sheet, "B"))
                #     current_page = current_page + 1
                #     current_sheet = current_sheet + direction
                #     continue
            
                # if current_sheet == self.booklet_sheets_count:
                #     imageA = images[n]
                #     self.images_in_booklet.append(BookletImage(imageA, right, 0, current_page, current_sheet, "A" if the_same_sheet_two_times == 0 else "B"))
                #     current_page = current_page + 1
                #     if n + 1 >= len(images):
                #         break
                #     the_same_sheet_two_times = the_same_sheet_two_times + 1
                #     if the_same_sheet_two_times == 2:
                #         direction = -1
                #         current_page = current_page + direction
                #     imageB = images[n + 1]
                #     self.images_in_booklet.append(BookletImage(imageB, left, 0, current_page, current_sheet, "B" if the_same_sheet_two_times == 0 else "A"))
                #     if the_same_sheet_two_times == 2:
                #         current_sheet = current_sheet + direction
                        
                    


    
    def return_next_image(self):
        return_now = self.currently_returnet_image
        self.currently_returnet_image = self.currently_returnet_image + 1
        return self.images_in_booklet[return_now]

class BookletImage:
    """One imge in booklet - so it is one file with coordinates where to place it"""
    path = ""
    edge = 0 #0 is snap to left, 1 is snap to right
    y = 0 #0 is snap to top, 1 is snap to bottom
    booklet_page = 0
    booklet_sheet = 0
    booklet_side = "" #Side A or Side Bs

    def __init__(self, path, edge, y, booklet_page, booklet_sheet, booklet_side):
        self.path = path
        self.edge = edge
        self.y = y
        self.booklet_page = booklet_page
        self.booklet_sheet = booklet_sheet
        self.booklet_side = booklet_side