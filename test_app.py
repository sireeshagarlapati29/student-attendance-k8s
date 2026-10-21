
import unittest
from app import app

class AttendanceTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Attendance System is running!", response.data)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_attendance(self):
        response = self.client.get("/attendance")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["attendance"], "Present")

if __name__ == "__main__":
    unittest.main()