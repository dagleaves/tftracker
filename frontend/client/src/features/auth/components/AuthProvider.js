import React, { Fragment , useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { checkAuth } from '@/features/auth';

export const AuthProvider = ({ children }) => {
    const dispatch = useDispatch();
    dispatch(checkAuth());

    return (
        <Fragment>
            {children}
        </Fragment>
    );
};