import unittest

from omg import sum, Booklet


class TestBooklet(unittest.TestCase):
    PRAWA = 1
    LEWA = 0
    A = "A"
    B = "B"

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

        
    def test_booklet_pages_count_should_be_four(self):
        b = Booklet(1, 1)
        self.assertEqual(b.booklet_pages_count, 4)

    def test_booklet_pages_count_should_be_eight(self):
        b = Booklet(5, 1)
        self.assertEqual(b.booklet_pages_count, 8)

    def test_booklet_pages_count_should_be_four_with_two_documents(self):
        b = Booklet(1, 2)
        self.assertEqual(b.booklet_pages_count, 4)

    def test_booklet_pages_count_should_be_eight_with_two_documents(self):
        b = Booklet(5, 2)
        self.assertEqual(b.booklet_pages_count, 8)

    # def test_one_image_should_be_at_right_side_of_first_booklet_page(self):
    #     b = Booklet(1, 1)
    #     images = ["01.jpg"]
        
    #     b.assign_images(images)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "01.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)

    # def test_second_image_should_be_at_left_side_of_second_booklet_page(self):
    #     b = Booklet(2, 1)
    #     images = ["01.jpg", "02.jpg"]
        
    #     b.assign_images(images)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "01.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 1)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "02.jpg")
    #     self.assertEqual(next_image.edge, self.LEWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 2)

    # def test_third_image_should_be_at_right_side_of_second_booklet_page(self):
    #     b = Booklet(3, 1)
    #     images = ["01.jpg", "02.jpg", "03.jpg"]
        
    #     b.assign_images(images)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "01.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 1)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "02.jpg")
    #     self.assertEqual(next_image.edge, self.LEWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 2)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "03.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 2)

    # def test_fourth_image_should_be_at_left_side_of_first_booklet_page(self):
    #     b = Booklet(4, 1)
    #     images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg"]
        
    #     b.assign_images(images)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "01.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 1)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "02.jpg")
    #     self.assertEqual(next_image.edge, self.LEWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 2)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "03.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 2)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "04.jpg")
    #     self.assertEqual(next_image.edge, self.LEWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 1)

    # def test_fifth_image_should_be_at_right_side_of_third_booklet_page(self):
    #     b = Booklet(5, 1)
    #     images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", "05.jpg"]
        
    #     b.assign_images(images)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "01.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 1)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "02.jpg")
    #     self.assertEqual(next_image.edge, self.LEWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 2)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "03.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 3)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "04.jpg")
    #     self.assertEqual(next_image.edge, self.LEWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 4)

    #     next_image = b.return_next_image()
    #     self.assertEqual(next_image.path, "05.jpg")
    #     self.assertEqual(next_image.edge, self.PRAWA)
    #     self.assertEqual(next_image.y, 0)
    #     self.assertEqual(next_image.booklet_page, 4)


    def test_sixth_image_should_be_at_left_side_of_fourth_booklet_page(self):
        b = Booklet(6, 1)
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
        b = Booklet(7, 1)
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



if __name__ == '__main__':
    unittest.main()
