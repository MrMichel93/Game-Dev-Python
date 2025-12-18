"""
Tests for Practice Problem 2: Particle System Functions
Run with: pytest test_practice_problem_2.py
"""

import pytest
from practice_problem_2_starter import (
    create_particles,
    update_particles,
    count_alive_particles,
    remove_dead_particles,
    get_particle_positions
)


class TestCreateParticles:
    """Tests for create_particles function"""
    
    def test_creates_correct_count(self):
        """Test creating correct number of particles"""
        particles = create_particles(5, 100, 200)
        assert len(particles) == 5
    
    def test_particle_structure(self):
        """Test particle has correct structure"""
        particles = create_particles(1, 100, 200)
        particle = particles[0]
        assert 'x' in particle
        assert 'y' in particle
        assert 'speed' in particle
        assert 'alive' in particle
    
    def test_particle_values(self):
        """Test particle has correct initial values"""
        particles = create_particles(1, 150, 250)
        particle = particles[0]
        assert particle['x'] == 150
        assert particle['y'] == 250
        assert particle['speed'] == 2
        assert particle['alive'] == True


class TestUpdateParticles:
    """Tests for update_particles function"""
    
    def test_updates_position(self):
        """Test particle positions are updated"""
        particles = [{'x': 100, 'y': 100, 'speed': 5, 'alive': True}]
        update_particles(particles)
        assert particles[0]['y'] == 105
    
    def test_marks_particle_dead(self):
        """Test particle marked dead when y > 600"""
        particles = [{'x': 100, 'y': 590, 'speed': 15, 'alive': True}]
        update_particles(particles)
        assert particles[0]['alive'] == False
    
    def test_keeps_particle_alive(self):
        """Test particle stays alive when y <= 600"""
        particles = [{'x': 100, 'y': 500, 'speed': 5, 'alive': True}]
        update_particles(particles)
        assert particles[0]['alive'] == True


class TestCountAliveParticles:
    """Tests for count_alive_particles function"""
    
    def test_counts_all_alive(self):
        """Test counting when all are alive"""
        particles = [{'alive': True}, {'alive': True}, {'alive': True}]
        assert count_alive_particles(particles) == 3
    
    def test_counts_mixed(self):
        """Test counting mixed alive/dead"""
        particles = [{'alive': True}, {'alive': False}, {'alive': True}]
        assert count_alive_particles(particles) == 2
    
    def test_counts_none_alive(self):
        """Test counting when none are alive"""
        particles = [{'alive': False}, {'alive': False}]
        assert count_alive_particles(particles) == 0
    
    def test_empty_list(self):
        """Test with empty list"""
        assert count_alive_particles([]) == 0


class TestRemoveDeadParticles:
    """Tests for remove_dead_particles function"""
    
    def test_removes_dead_particles(self):
        """Test removing dead particles"""
        particles = [{'alive': True}, {'alive': False}, {'alive': True}]
        result = remove_dead_particles(particles)
        assert len(result) == 2
        assert all(p['alive'] for p in result)
    
    def test_keeps_all_alive(self):
        """Test when all particles are alive"""
        particles = [{'alive': True}, {'alive': True}]
        result = remove_dead_particles(particles)
        assert len(result) == 2
    
    def test_removes_all_dead(self):
        """Test when all particles are dead"""
        particles = [{'alive': False}, {'alive': False}]
        result = remove_dead_particles(particles)
        assert len(result) == 0


class TestGetParticlePositions:
    """Tests for get_particle_positions function"""
    
    def test_extracts_positions(self):
        """Test extracting positions"""
        particles = [{'x': 10, 'y': 20}, {'x': 30, 'y': 40}]
        result = get_particle_positions(particles)
        assert result == [(10, 20), (30, 40)]
    
    def test_returns_tuples(self):
        """Test returns list of tuples"""
        particles = [{'x': 5, 'y': 10}]
        result = get_particle_positions(particles)
        assert isinstance(result[0], tuple)
    
    def test_empty_list(self):
        """Test with empty list"""
        result = get_particle_positions([])
        assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
