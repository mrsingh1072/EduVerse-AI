import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'

export default function AuthLayout({ children }) {
  return (
    <div className="min-h-screen relative overflow-hidden pt-24 pb-16">
      {/* Background Gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-cream via-white to-cream" />

      {/* Radial Gradient Spotlight */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            'radial-gradient(ellipse 1200px 600px at 50% 30%, rgba(47, 93, 80, 0.08) 0%, transparent 70%)',
        }}
      />

      {/* Floating Gradient Orbs */}
      <motion.div
        animate={{
          y: [0, 30, 0],
          x: [0, 15, 0],
        }}
        transition={{
          duration: 12,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
        className="absolute top-20 right-20 w-72 h-72 bg-gradient-to-br from-green-primary/20 to-green-primary/5 rounded-full blur-3xl -z-0"
      />

      <motion.div
        animate={{
          y: [0, -40, 0],
          x: [0, -20, 0],
        }}
        transition={{
          duration: 15,
          repeat: Infinity,
          ease: 'easeInOut',
          delay: 1,
        }}
        className="absolute bottom-32 left-10 w-80 h-80 bg-gradient-to-br from-gold/15 to-gold/5 rounded-full blur-3xl -z-0"
      />

      <motion.div
        animate={{
          y: [0, 25, 0],
          x: [0, -25, 0],
        }}
        transition={{
          duration: 18,
          repeat: Infinity,
          ease: 'easeInOut',
          delay: 2,
        }}
        className="absolute top-1/2 left-1/4 w-64 h-64 bg-gradient-to-br from-green-secondary/10 to-transparent rounded-full blur-3xl -z-0"
      />

      {/* Navbar */}
      <nav className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-6 md:px-12 py-4 bg-white/50 backdrop-blur-md border-b border-white/80">
        <Link
          to="/"
          className="text-2xl font-bold bg-gradient-to-r from-green-primary to-green-secondary bg-clip-text text-transparent hover:scale-105 transition-transform"
        >
          EduVerse AI
        </Link>
        <Link
          to="/"
          className="text-gray-600 hover:text-green-primary font-semibold transition-colors"
        >
          Back to Home
        </Link>
      </nav>

      {/* Main Content */}
      <div className="relative z-10 flex items-center justify-center min-h-screen px-4 sm:px-6">
        <div className="w-full max-w-4xl">{children}</div>
      </div>
    </div>
  )
}
