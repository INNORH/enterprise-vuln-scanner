from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

class Organization(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    users = relationship('User', back_populates='organization')
    assets = relationship('Asset', back_populates='organization')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    organization = relationship('Organization', back_populates='users')
    scans = relationship('Scan', back_populates='user')

class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    vulnerabilities = relationship('Vulnerability', back_populates='asset')
    organization = relationship('Organization', back_populates='assets')

class Scan(Base):
    __tablename__ = 'scans'
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    vulnerabilities = relationship('Vulnerability', back_populates='scan')
    asset = relationship('Asset', back_populates='scans')
    user = relationship('User', back_populates='scans')

class Vulnerability(Base):
    __tablename__ = 'vulnerabilities'
    id = Column(Integer, primary_key=True)
    scan_id = Column(Integer, ForeignKey('scans.id'))
    description = Column(Text, nullable=False)
    severity = Column(Enum('low', 'medium', 'high', name='severity_levels'))
    created_at = Column(DateTime, default=datetime.utcnow)
    scan = relationship('Scan', back_populates='vulnerabilities')

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    vulnerability_id = Column(Integer, ForeignKey('vulnerabilities.id'))
    acknowledged = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    vulnerability = relationship('Vulnerability')

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship('User')

class ComplianceReport(Base):
    __tablename__ = 'compliance_reports'
    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    report_data = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    organization = relationship('Organization')