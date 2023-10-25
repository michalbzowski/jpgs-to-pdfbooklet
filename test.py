import unittest

from booklet import Booklet


class TestBooklet(unittest.TestCase):
    PRAWA = 1
    LEWA = 0
    A = "A"
    B = "B"

        
    def test_booklet_pages_count_should_be_four(self):
        b = Booklet(1)
        self.assertEqual(b.booklet_pages_count, 4)

    def test_booklet_pages_count_should_be_eight(self):
        b = Booklet(5)
        self.assertEqual(b.booklet_pages_count, 8)

    def test_booklet_pages_count_should_be_four_with_two_documents(self):
        b = Booklet(1)
        self.assertEqual(b.booklet_pages_count, 4)

    def test_booklet_pages_count_should_be_eight_with_two_documents(self):
        b = Booklet(5)
        self.assertEqual(b.booklet_pages_count, 8)

    def test_one_image_should_be_at_right_side_of_first_booklet_page(self):
        b = Booklet(1)
        images = ["01.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)
        self.assertEqual(next_image.booklet_sheet, 1)

    def test_second_image_should_be_at_left_side_of_second_booklet_page(self):
        b = Booklet(2)
        images = ["01.jpg", "02.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)
        self.assertEqual(next_image.booklet_sheet, 1)

    def test_third_image_should_be_at_right_side_of_second_booklet_page(self):
        b = Booklet(3)
        images = ["01.jpg", "02.jpg", "03.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)

    def test_fourth_image_should_be_at_left_side_of_first_booklet_page(self):
        b = Booklet(4)
        images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "04.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)

    def test_fifth_image_should_be_at_right_side_of_third_booklet_page(self):
        b = Booklet(5)
        images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", "05.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "04.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "05.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)


    def test_sixth_image_should_be_at_left_side_of_fourth_booklet_page(self):
        b = Booklet(6)
        images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", "05.jpg", "06.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "04.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)


        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "05.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)
        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "06.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

    def test_fifth_image_should_be_at_right_side_of_third_booklet_page(self):
        b = Booklet(7)
        images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", "05.jpg", "06.jpg", "07.jpg"]
        
        b.assign_images(images)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "04.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)

########

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "05.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)
        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "06.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "07.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)
        self.assertEqual(next_image.booklet_sheet, 1)

    def nine(self):
        b = Booklet(7)
        images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", "05.jpg", "06.jpg", "07.jpg", "08.jpg", "09.jpg"]
        
        b.assign_images(images)

###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)
        self.assertEqual(next_image.booklet_sheet, 1)
###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "04.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 3)
###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "05.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 5)
        self.assertEqual(next_image.booklet_sheet, 3)
        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "06.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 6)
        self.assertEqual(next_image.booklet_sheet, 3)

#######

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "07.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 6)
        self.assertEqual(next_image.booklet_sheet, 3)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "08.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 5)
        self.assertEqual(next_image.booklet_sheet, 3)

###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "09.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)

    def test_current_koscielne_ksiazeczki(self):
        b = Booklet(26)
        images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", "05.jpg", "06.jpg", "07.jpg", "08.jpg", "09.jpg", 
                  "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg",
                  "19.jpg", "20.jpg", "21.jpg", "22.jpg", "23.jpg", "24.jpg", "25.jpg", "26.jpg"]
        
        b.assign_images(images)

###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "01.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 1)
        self.assertEqual(next_image.booklet_sheet, 1)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "02.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 2)
        self.assertEqual(next_image.booklet_sheet, 1)
###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "03.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "04.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)
###
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "05.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 5)
        self.assertEqual(next_image.booklet_sheet, 3)
        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "06.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 6)
        self.assertEqual(next_image.booklet_sheet, 3)



        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "07.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 7)
        self.assertEqual(next_image.booklet_sheet, 4)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "08.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 8)
        self.assertEqual(next_image.booklet_sheet, 4)


        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "09.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 9)
        self.assertEqual(next_image.booklet_sheet, 5)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "10.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 10)
        self.assertEqual(next_image.booklet_sheet, 5)

        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "11.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 11)
        self.assertEqual(next_image.booklet_sheet, 6)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "12.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 12)
        self.assertEqual(next_image.booklet_sheet, 6)

        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "13.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 13)
        self.assertEqual(next_image.booklet_sheet, 7)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "14.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 14)
        self.assertEqual(next_image.booklet_sheet, 7)

        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "15.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 14)
        self.assertEqual(next_image.booklet_sheet, 7)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "16.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 13)
        self.assertEqual(next_image.booklet_sheet, 7)

        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "17.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 12)
        self.assertEqual(next_image.booklet_sheet, 6)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "18.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page,11)
        self.assertEqual(next_image.booklet_sheet, 6)

        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "19.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 10)
        self.assertEqual(next_image.booklet_sheet, 5)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "20.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 9)
        self.assertEqual(next_image.booklet_sheet, 5)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "21.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 8)
        self.assertEqual(next_image.booklet_sheet, 4)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "22.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 7)
        self.assertEqual(next_image.booklet_sheet, 4)

        
        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "23.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 6)
        self.assertEqual(next_image.booklet_sheet, 3)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "24.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 5)
        self.assertEqual(next_image.booklet_sheet, 3)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "25.jpg")
        self.assertEqual(next_image.edge, self.PRAWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 4)
        self.assertEqual(next_image.booklet_sheet, 2)

        next_image = b.return_next_image()
        self.assertEqual(next_image.path, "26.jpg")
        self.assertEqual(next_image.edge, self.LEWA)
        self.assertEqual(next_image.y, 0)
        self.assertEqual(next_image.booklet_page, 3)
        self.assertEqual(next_image.booklet_sheet, 2)

        #R2,1 i L1,1 są puste - przetestować to?


if __name__ == '__main__':
    unittest.main()
