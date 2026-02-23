import { useState } from 'react'

function ProfileDetail({ profile, onBack }) {
  const [interestSent, setInterestSent] = useState(false)

  if (!profile) return null

  const handleSendInterest = () => {
    setInterestSent(true)
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <button 
        onClick={onBack}
        className="flex items-center text-rose-600 hover:text-rose-700 mb-6 font-medium"
      >
        ← Back to Profiles
      </button>

      <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
        <div className="relative bg-gradient-to-r from-rose-500 via-pink-500 to-rose-400 h-56">
          <div className="absolute -bottom-16 left-8">
            <div className="w-32 h-32 bg-white rounded-2xl shadow-xl flex items-center justify-center text-7xl border-4 border-white">
              {profile.image}
            </div>
          </div>
          {profile.verified && (
            <span className="absolute top-4 right-4 bg-green-500 text-white text-sm px-3 py-1 rounded-full flex items-center gap-1">
              ✓ Verified Profile
            </span>
          )}
        </div>
        
        <div className="pt-20 p-8">
          <div className="flex flex-wrap justify-between items-start gap-4 mb-8">
            <div>
              <h1 className="text-3xl font-bold text-gray-800">{profile.name}</h1>
              <p className="text-gray-600 text-lg">{profile.age} years old • {profile.height}</p>
              <p className="text-gray-500">{profile.location}</p>
            </div>
            <div className="flex gap-3">
              <button 
                onClick={handleSendInterest}
                disabled={interestSent}
                className={`px-6 py-2.5 rounded-lg font-medium transition ${interestSent ? 'bg-green-500 text-white' : 'bg-rose-500 text-white hover:bg-rose-600'}`}
              >
                {interestSent ? '✓ Interest Sent' : 'Send Interest'}
              </button>
              <button className="border-2 border-rose-500 text-rose-500 px-6 py-2.5 rounded-lg font-medium hover:bg-rose-50 transition">
                💬 Chat
              </button>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-gray-50 p-6 rounded-xl">
              <h2 className="text-xl font-semibold text-gray-800 mb-4 flex items-center gap-2">
                👤 Personal Details
              </h2>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-gray-500">Profession</span>
                  <span className="font-medium">{profile.profession}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Height</span>
                  <span className="font-medium">{profile.height || 'Not specified'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Location</span>
                  <span className="font-medium">{profile.location}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Education</span>
                  <span className="font-medium">{profile.education}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-500">Religion</span>
                  <span className="font-medium">{profile.religion}</span>
                </div>
              </div>
            </div>

            <div className="bg-gray-50 p-6 rounded-xl">
              <h2 className="text-xl font-semibold text-gray-800 mb-4 flex items-center gap-2">
                📝 About Me
              </h2>
              <p className="text-gray-600 leading-relaxed">
                Hello! I'm {profile.name}, a {profile.profession} based in {profile.location}. 
                I have completed my {profile.education}. I'm looking for someone who shares similar values 
                and is looking for a meaningful relationship. I believe in traditional values while 
                maintaining a modern outlook on life. In my free time, I enjoy traveling, reading, and 
                spending time with family.
              </p>
            </div>
          </div>

          <div className="mt-8 p-6 bg-gradient-to-r from-rose-50 to-pink-50 rounded-xl">
            <h2 className="text-xl font-semibold text-gray-800 mb-4 flex items-center gap-2">
              💕 Partner Preferences
            </h2>
            <div className="grid md:grid-cols-4 gap-4">
              <div className="bg-white p-4 rounded-lg text-center">
                <p className="text-gray-500 text-sm">Age</p>
                <p className="font-semibold text-rose-600">22-30 years</p>
              </div>
              <div className="bg-white p-4 rounded-lg text-center">
                <p className="text-gray-500 text-sm">Height</p>
                <p className="font-semibold text-rose-600">5'2" - 5'10"</p>
              </div>
              <div className="bg-white p-4 rounded-lg text-center">
                <p className="text-gray-500 text-sm">Profession</p>
                <p className="font-semibold text-rose-600">Professional</p>
              </div>
              <div className="bg-white p-4 rounded-lg text-center">
                <p className="text-gray-500 text-sm">Location</p>
                <p className="font-semibold text-rose-600">Any Indian City</p>
              </div>
            </div>
          </div>

          <div className="mt-6 flex flex-wrap gap-3">
            <button className="flex-1 bg-rose-100 text-rose-700 py-3 rounded-lg font-medium hover:bg-rose-200 transition">
              📞 View Contact
            </button>
            <button className="flex-1 bg-gray-100 text-gray-700 py-3 rounded-lg font-medium hover:bg-gray-200 transition">
              ⭐ Shortlist
            </button>
            <button className="flex-1 bg-gray-100 text-gray-700 py-3 rounded-lg font-medium hover:bg-gray-200 transition">
              🚫 Not Interested
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProfileDetail
