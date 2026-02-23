import { useState } from 'react'
import { profileImages } from '../data/profiles'

function CreateProfile({ onSubmit, onCancel }) {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    profession: '',
    location: '',
    height: '',
    education: '',
    religion: 'Hindu',
    image: '👨‍💼',
    about: ''
  })

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit(formData)
  }

  const locations = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi', 'Kolkata']
  const religions = ['Hindu', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain', 'Other']
  const professions = ['Software Engineer', 'Doctor', 'Teacher', 'Engineer', 'Business Owner', 'Designer', 'Marketing Manager', 'CA', 'Banker', 'Architect', 'Data Scientist', 'Lawyer', 'Other']

  return (
    <div className="max-w-3xl mx-auto px-4 py-8">
      <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
        <div className="bg-gradient-to-r from-rose-500 to-pink-500 py-8 text-center">
          <h1 className="text-3xl font-bold text-white">Create Your Profile</h1>
          <p className="text-white/80 mt-2">Fill in your details to find your perfect match</p>
        </div>

        <form onSubmit={handleSubmit} className="p-8">
          <div className="mb-8 text-center">
            <label className="block text-gray-700 font-semibold mb-3">Choose Your Avatar</label>
            <div className="flex flex-wrap justify-center gap-3">
              {profileImages.map((img) => (
                <button
                  key={img}
                  type="button"
                  onClick={() => setFormData({ ...formData, image: img })}
                  className={`w-16 h-16 rounded-full text-3xl flex items-center justify-center transition ${
                    formData.image === img 
                      ? 'bg-rose-100 ring-2 ring-rose-500 scale-110' 
                      : 'bg-gray-100 hover:bg-gray-200'
                  }`}
                >
                  {img}
                </button>
              ))}
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <label className="block text-gray-700 font-medium mb-2">Full Name *</label>
              <input
                type="text"
                name="name"
                required
                value={formData.name}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
                placeholder="Enter your name"
              />
            </div>

            <div>
              <label className="block text-gray-700 font-medium mb-2">Age *</label>
              <input
                type="number"
                name="age"
                required
                min="18"
                max="50"
                value={formData.age}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
                placeholder="Enter your age"
              />
            </div>

            <div>
              <label className="block text-gray-700 font-medium mb-2">Profession *</label>
              <select
                name="profession"
                required
                value={formData.profession}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
              >
                <option value="">Select Profession</option>
                {professions.map(prof => (
                  <option key={prof} value={prof}>{prof}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-gray-700 font-medium mb-2">Location *</label>
              <select
                name="location"
                required
                value={formData.location}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
              >
                <option value="">Select Location</option>
                {locations.map(loc => (
                  <option key={loc} value={loc}>{loc}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-gray-700 font-medium mb-2">Height</label>
              <select
                name="height"
                value={formData.height}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
              >
                <option value="">Select Height</option>
                {["4'6\"", "4'7\"", "4'8\"", "4'9\"", "4'10\"", "4'11\"", "5'0\"", "5'1\"", "5'2\"", "5'3\"", "5'4\"", "5'5\"", "5'6\"", "5'7\"", "5'8\"", "5'9\"", "5'10\"", "5'11\"", "6'0\"", "6'1\"", "6'2\""].map(h => (
                  <option key={h} value={h}>{h}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-gray-700 font-medium mb-2">Education *</label>
              <input
                type="text"
                name="education"
                required
                value={formData.education}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
                placeholder="e.g., B.Tech, MBBS, MBA"
              />
            </div>

            <div>
              <label className="block text-gray-700 font-medium mb-2">Religion *</label>
              <select
                name="religion"
                required
                value={formData.religion}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
              >
                {religions.map(rel => (
                  <option key={rel} value={rel}>{rel}</option>
                ))}
              </select>
            </div>
          </div>

          <div className="mt-6">
            <label className="block text-gray-700 font-medium mb-2">About Yourself</label>
            <textarea
              name="about"
              value={formData.about}
              onChange={handleChange}
              rows="4"
              className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500"
              placeholder="Tell us about yourself, your interests, and what you're looking for..."
            />
          </div>

          <div className="flex gap-4 mt-8">
            <button
              type="submit"
              className="flex-1 bg-gradient-to-r from-rose-500 to-pink-500 text-white py-3 rounded-lg font-semibold hover:from-rose-600 hover:to-pink-600 transition"
            >
              Create Profile
            </button>
            <button
              type="button"
              onClick={onCancel}
              className="flex-1 border-2 border-gray-300 text-gray-600 py-3 rounded-lg font-semibold hover:bg-gray-100 transition"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CreateProfile
