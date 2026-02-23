function Home({ onNavigate }) {
  return (
    <div>
      <section className="relative bg-gradient-to-r from-rose-600 via-rose-500 to-pink-500 text-white py-32 overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-10 left-10 text-8xl">💕</div>
          <div className="absolute top-20 right-20 text-6xl">💍</div>
          <div className="absolute bottom-10 left-1/4 text-7xl">❤️</div>
          <div className="absolute bottom-20 right-1/3 text-5xl">✨</div>
        </div>
        <div className="max-w-7xl mx-auto px-4 text-center relative z-10">
          <h1 className="text-5xl md:text-6xl font-bold mb-6 animate-fadeIn">
            Find Your <span className="text-rose-200">Perfect Partner</span>
          </h1>
          <p className="text-xl md:text-2xl mb-8 opacity-90 max-w-2xl mx-auto">
            Join 2+ million happy couples who found their soulmate on ShaadiZone
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <button 
              onClick={() => onNavigate('profiles')}
              className="bg-white text-rose-600 px-8 py-4 rounded-full font-semibold text-lg hover:bg-rose-50 transition shadow-lg hover:shadow-xl transform hover:-translate-y-1"
            >
              Start Searching Free
            </button>
            <button className="border-2 border-white text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-white hover:text-rose-600 transition">
              Register Free
            </button>
          </div>
          <div className="mt-8 text-sm opacity-80">
            <p>Made with ❤️ by <span className="font-semibold">Animesh</span></p>
          </div>
          <div className="mt-8 flex justify-center gap-8 text-sm">
            <div className="text-center">
              <p className="text-3xl font-bold">2M+</p>
              <p className="opacity-80">Members</p>
            </div>
            <div className="text-center">
              <p className="text-3xl font-bold">50K+</p>
              <p className="opacity-80">Success Stories</p>
            </div>
            <div className="text-center">
              <p className="text-3xl font-bold">1000+</p>
              <p className="opacity-80">Daily Matches</p>
            </div>
          </div>
        </div>
      </section>

      <section className="py-20 max-w-7xl mx-auto px-4">
        <h2 className="text-3xl font-bold text-center text-gray-800 mb-4">Find Your Perfect Match</h2>
        <p className="text-center text-gray-600 mb-12 max-w-xl mx-auto">
          Search through thousands of verified profiles based on your preferences
        </p>
        
        <div className="grid md:grid-cols-4 gap-4 mb-12">
          {['Age', 'Religion', 'Location', 'Profession'].map((filter, i) => (
            <select key={filter} className="p-4 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-rose-500 bg-white">
              <option>{filter}</option>
            </select>
          ))}
        </div>
        
        <div className="text-center">
          <button 
            onClick={() => onNavigate('profiles')}
            className="bg-rose-500 text-white px-8 py-3 rounded-full font-semibold hover:bg-rose-600 transition"
          >
            Search Now
          </button>
        </div>
      </section>

      <section className="py-20 bg-gradient-to-r from-rose-500 to-pink-500 text-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold mb-6">Register Free & Create Your Profile</h2>
              <ul className="space-y-4">
                {['Create your profile in minutes', 'Get verified badge', 'Connect with compatible matches', 'Chat with genuine people'].map(item => (
                  <li key={item} className="flex items-center gap-3">
                    <span className="text-2xl">✓</span>
                    <span className="text-lg">{item}</span>
                  </li>
                ))}
              </ul>
              <button className="mt-8 bg-white text-rose-600 px-8 py-3 rounded-full font-semibold text-lg hover:bg-rose-50 transition">
                Create Free Profile
              </button>
            </div>
            <div className="hidden md:block">
              <div className="bg-white/10 backdrop-blur rounded-2xl p-8">
                <div className="bg-white rounded-xl p-6 text-gray-800">
                  <div className="flex items-center gap-4 mb-4">
                    <div className="w-16 h-16 bg-rose-100 rounded-full flex items-center justify-center text-3xl">👩‍💻</div>
                    <div>
                      <p className="font-semibold">Priya, 26</p>
                      <p className="text-gray-500 text-sm">Software Engineer, Mumbai</p>
                    </div>
                  </div>
                  <p className="text-gray-600 text-sm">"Found my perfect match here! We're getting married next month."</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="py-20 max-w-7xl mx-auto px-4">
        <h2 className="text-3xl font-bold text-center text-gray-800 mb-12">Why Choose ShaadiZone?</h2>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            { icon: '🔍', title: 'Smart Matching', desc: 'Our AI algorithm finds compatible matches based on your preferences' },
            { icon: '🛡️', title: 'Verified Profiles', desc: 'All profiles are manually verified for authenticity' },
            { icon: '💬', title: 'Easy Communication', desc: 'Connect with potential matches through our secure messaging' },
            { icon: '📱', title: 'Mobile Friendly', desc: 'Access your matches anywhere on any device' },
            { icon: '🔒', title: 'Privacy First', desc: 'Your data is secure with us' },
            { icon: '❤️', title: 'Success Stories', desc: '50,000+ couples found love here' },
          ].map(({ icon, title, desc }) => (
            <div key={title} className="bg-white p-8 rounded-xl shadow-md hover:shadow-xl transition text-center group">
              <div className="text-5xl mb-4 group-hover:scale-110 transition">{icon}</div>
              <h3 className="text-xl font-semibold mb-2">{title}</h3>
              <p className="text-gray-600">{desc}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="bg-rose-50 py-20">
        <div className="max-w-7xl mx-auto px-4">
          <h2 className="text-3xl font-bold text-center text-gray-800 mb-12">Success Stories</h2>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { quote: "We found each other on ShaadiZone and knew instantly this was meant to be.", names: "Rahul & Priya", emoji: "💕" },
              { quote: "After trying other apps, ShaadiZone helped me find my perfect match.", names: "Amit & Sneha", emoji: "💍" },
              { quote: "Best decision I made was to join ShaadiZone. We're now happily married!", names: "Raj & Kavya", emoji: "❤️" },
            ].map(({ quote, names, emoji }) => (
              <div key={names} className="bg-white p-8 rounded-xl shadow-md">
                <div className="text-4xl mb-4">{emoji}</div>
                <p className="text-gray-600 italic mb-4 text-lg">"{quote}"</p>
                <p className="font-semibold text-rose-600">- {names}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  )
}

export default Home
