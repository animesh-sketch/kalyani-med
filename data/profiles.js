import { useState } from 'react'

const initialProfiles = [
  { id: 1, name: 'Priya Sharma', age: 26, profession: 'Software Engineer', location: 'Mumbai', height: "5'6\"", education: 'B.Tech', religion: 'Hindu', image: '👩‍💻', verified: true },
  { id: 2, name: 'Rahul Verma', age: 28, profession: 'Doctor', location: 'Delhi', height: "5'10\"", education: 'MBBS', religion: 'Hindu', image: '👨‍⚕️', verified: true },
  { id: 3, name: 'Anjali Patel', age: 24, profession: 'Teacher', location: 'Ahmedabad', height: "5'3\"", education: 'M.A. B.Ed', religion: 'Hindu', image: '👩‍🏫', verified: false },
  { id: 4, name: 'Vikram Singh', age: 30, profession: 'Business Owner', location: 'Jaipur', height: "5'11\"", education: 'MBA', religion: 'Hindu', image: '👨‍💼', verified: true },
  { id: 5, name: 'Meera Nair', age: 27, profession: 'Designer', location: 'Bangalore', height: "5'4\"", education: 'B.Des', religion: 'Hindu', image: '👩‍🎨', verified: true },
  { id: 6, name: 'Arjun Menon', age: 29, profession: 'Engineer', location: 'Kochi', height: "5'9\"", education: 'B.Tech', religion: 'Hindu', image: '👨‍🔧', verified: false },
  { id: 7, name: 'Kavya Reddy', age: 25, profession: 'Marketing Manager', location: 'Hyderabad', height: "5'5\"", education: 'MBA', religion: 'Hindu', image: '👩‍💼', verified: true },
  { id: 8, name: 'Dev Kapoor', age: 31, profession: 'CA', location: 'Mumbai', height: "5'8\"", education: 'CA', religion: 'Hindu', image: '👨‍💼', verified: true },
  { id: 9, name: 'Sneha Iyer', age: 23, profession: 'Banker', location: 'Chennai', height: "5'2\"", education: 'B.Com', religion: 'Hindu', image: '👩‍💼', verified: true },
  { id: 10, name: 'Karan Malhotra', age: 27, profession: 'Architect', location: 'Pune', height: "5'10\"", education: 'B.Arch', religion: 'Hindu', image: '👨‍🎨', verified: false },
  { id: 11, name: 'Riya Gupta', age: 26, profession: 'Data Scientist', location: 'Bangalore', height: "5'4\"", education: 'M.Sc', religion: 'Hindu', image: '👩‍🔬', verified: true },
  { id: 12, name: 'Aditya Sharma', age: 32, profession: 'Lawyer', location: 'Delhi', height: "6'0\"", education: 'LLB', religion: 'Hindu', image: '👨‍⚖️', verified: true },
]

const profileImages = ['👨‍💼', '👩‍💼', '👨‍💻', '👩‍💻', '👨‍⚕️', '👩‍⚕️', '👨‍🎓', '👩‍🎓', '👨‍🔬', '👩‍🔬', '👨‍🏫', '👩‍🏫', '👨‍🎨', '👩‍🎨', '👨‍💼', '👩‍💼']

export { initialProfiles, profileImages }
